# -*- coding: utf-8 -*-
"""
    Added by shaozhe.wang(154082)
    at 2018/2/14 11:20
    ---------------------------------
"""
import datetime
import md5
import threading

from common.torndb import Connection
from my_thread import MyThread
from functools import wraps, partial
from multiprocessing import Queue, Process
import re
import sys

import signal

from common.etl.etl_exception import TimeoutException

import time

from arrow import arrow
from MySQLdb import OperationalError

# import torndb
from common import torndb
from common.etl import etl_db
from common.db_config import DB_CONFIG
from common.sls_log_service import get_logger

DEFAULT_ETL_TIMEOUT = 600  # second
DEFAULT_QUERY_TIMEOUT = 30  # second
DEFAULT_CONNECT_TIMEOUT = 60  # second


def db_retry(retry_count=3):
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(*args, **kwargs):
            for i in xrange(retry_count):
                try:
                    res = func(*args, **kwargs)
                except OperationalError as e:
                    print "DB opertion failed, try count: %s" % (i + 1)
                    args[0].rebuild_db_connection()
                else:
                    return res

        return return_wrapper

    return func_wrapper


def _handle_timeout(args, signum=None, frame=None, rebuild_db_connection=False):
    if isinstance(args[0], DBBase):
        worker = args[0]
        # worker.thread_logger("Exec sql timeout!", "Argument: %s" % json.dumps(args))
        if rebuild_db_connection:
            worker.rebuild_db_connection()
    else:
        # print("Base", "Exec sql timeout!", "Argument: %s" % json.dumps(args))
        print("Base", "Exec sql timeout!")
    raise TimeoutException


def timeout(seconds=DEFAULT_ETL_TIMEOUT):
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, partial(_handle_timeout, args))
            signal.alarm(seconds)
            try:
                res = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return res

        return return_wrapper

    return func_wrapper


def thread_timeout(seconds=DEFAULT_ETL_TIMEOUT, rebuild_db_connection=False):
    def func_wrapper(func):
        def exception_capture_wrapper(func, queue, *args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                # print(sys.exc_info())
                queue.put(sys.exc_info())

        @wraps(func)
        def wrapper(*args, **kwargs):
            exception_queue = Queue()
            exception_wrapper = partial(exception_capture_wrapper, func, exception_queue)
            t = MyThread(target=exception_wrapper, args=args, kwargs=kwargs)
            t.start()
            t.join(seconds)
            if t.is_alive():
                _handle_timeout(args, rebuild_db_connection=True)
                raise TimeoutException
            if not exception_queue.empty():
                exc_type, exc_obj, exc_trace = exception_queue.get()
                raise exc_type(exc_obj)
            return t.get_result()

        return wrapper

    return func_wrapper


def thread_dynamic_timeout(rebuild_db_connection=False):
    def func_wrapper(func):
        def exception_capture_wrapper(func, queue, *args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                # print(sys.exc_info())
                queue.put(sys.exc_info())

        @wraps(func)
        def wrapper(*args, **kwargs):
            exception_queue = Queue()
            exception_wrapper = partial(exception_capture_wrapper, func, exception_queue)
            t = MyThread(target=exception_wrapper, args=args, kwargs=kwargs)
            t.start()
            t.join(args[1])
            if t.is_alive():
                _handle_timeout(args, rebuild_db_connection=True)
                t._Thread_stop()
                raise TimeoutException
            if not exception_queue.empty():
                exc_type, exc_obj, exc_trace = exception_queue.get()
                raise exc_type(exc_obj)
            return t.get_result()

        return wrapper

    return func_wrapper


def process_timeout(seconds=DEFAULT_ETL_TIMEOUT):
    def func_wrapper(func):
        def db_action(sql, db_name, func_name, execption_queue, result_queue):
            try:
                db_config = DB_CONFIG[db_name]
                db_client = torndb.Connection(
                    db_config["HOST"] + ":" + str(db_config["PORT"]),
                    db_config["DB"],
                    db_config["USER"],
                    db_config["PWD"],
                    time_zone='+8:00')
                if db_name:
                    func = getattr(db_client, func_name)
                    result_queue.put(func(sql))
            except Exception as e:
                print(e)
                # print(sys.exc_info())
                execption_queue.put(sys.exc_info())
            finally:
                db_client.close()

        @wraps(func)
        def wrapper(*args, **kwargs):
            exception_queue = Queue()
            result_queue = Queue()
            dbbase = args[0]
            sql = args[1]
            seconds = DEFAULT_QUERY_TIMEOUT
            if len(args) > 2:
                seconds = args[2]
            db_name = None
            if len(args) > 3:
                db_name = args[3]
            func_name = str(func.func_name).split("_")[0]
            p = Process(target=db_action, args=(sql, db_name if db_name else dbbase.db_name, func_name, exception_queue, result_queue),
                        kwargs=kwargs)
            p.start()
            p.join(seconds)
            if p.is_alive():
                p.terminate()
                raise TimeoutException
            if not exception_queue.empty():
                exc_type, exc_obj, exc_trace = exception_queue.get()
                raise exc_type(exc_obj)
            if result_queue.empty():
                return None
            return result_queue.get(block=False)

        return wrapper

    return func_wrapper


class DBBase(object):
    def __init__(self, config):
        self.db_client = {}
        self.db_name = None
        if config:
            self.__init_db(config)
        self.debug = False
        self.logger = get_logger()

    def __init_db(self, config):
        self.db_client = {}
        # print "Start init db: %s" % config
        if isinstance(config, dict):
            self.debug = config.get("debug_mode", False)
            # init db clients.
            for name, db_config in config["vnet_db"].iteritems():
                self.db_client[name] = torndb.Connection(db_config["db_host"],
                                                         db_config["database"],
                                                         db_config["user"], db_config["passwd"],
                                                         time_zone='+8:00',
                                                         connect_timeout=DEFAULT_CONNECT_TIMEOUT)
            self.config = config
        elif isinstance(config, (str, unicode)):
            db_names = config.split(",")
            self.db_name = db_names[0] if len(db_names) == 1 else None
            for db_name in db_names:
                if db_name not in DB_CONFIG:
                    raise Exception("DB config not found for : " + db_name)
                db_config = DB_CONFIG[db_name]
                self.db_client[db_name] = torndb.Connection(db_config["HOST"] + ":" + str(db_config["PORT"]),
                                                            db_config["DB"],
                                                            db_config["USER"],
                                                            db_config["PWD"],
                                                            time_zone='+8:00',
                                                            connect_timeout=DEFAULT_CONNECT_TIMEOUT)
        elif isinstance(config, list):
            self.db_name = config[0] if len(config) == 1 else None
            for db_name in config:
                if not db_name:
                    continue
                if db_name not in DB_CONFIG:
                    raise Exception("DB config not found for : " + db_name)
                db_config = DB_CONFIG[db_name]
                self.db_client[db_name] = torndb.Connection(db_config["HOST"] + ":" + str(db_config["PORT"]),
                                                            db_config["DB"],
                                                            db_config["USER"],
                                                            db_config["PWD"],
                                                            time_zone='+8:00',
                                                            connect_timeout=DEFAULT_CONNECT_TIMEOUT)

    def get_db_client(self, db_name):
        if db_name not in self.db_client:
            raise RuntimeError("Database connection of %s not found!" % db_name)
        return self.db_client[db_name]

    @staticmethod
    def get_new_db_client(db_name):
        if db_name not in DB_CONFIG:
            raise Exception("DB config not found for : " + db_name)
        db_config = DB_CONFIG[db_name]
        new_client = torndb.Connection(db_config["HOST"] + ":" + str(db_config["PORT"]),
                                       db_config["DB"],
                                       db_config["USER"],
                                       db_config["PWD"],
                                       time_zone='+8:00')
        return new_client

    @staticmethod
    def get_new_db_client_by_config(host, port, db_name, user, pwd):
        new_client = torndb.Connection(host + ":" + str(port),
                                       db_name,
                                       user,
                                       pwd,
                                       time_zone='+8:00')
        return new_client

    def close(self):
        self.close_db_connection()

    def close_db_connection(self):
        for db_client in self.db_client.itervalues():
            db_client.close()

    def rebuild_db_connection(self, db=None):
        if db:
            self.db_client[db].reconnect()
        else:
            for db_client in self.db_client.itervalues():
                db_client.reconnect()

    def write_db_with_update_and_delete_outdated(self, db, table, result, update_time_column='modified_at',
                                                 expire_minute=5, ignore_columns=None):
        """Write data to db and delete outdated data.
            insert into on duplicate key update
            ignore_columns is list or str separated by comma
        """
        def _check_user_params(params, primary_key):
            user_primary_key = [k for k in params.keys() if k in primary_key]
            assert len(user_primary_key) == len(primary_key), 'User passed parameter error, the lack of a primary key'

        ignore_columns = list() if ignore_columns is None else ignore_columns
        if isinstance(ignore_columns, str):
            ignore_columns = ignore_columns.split(',')
        create_sql = self.query_p(db, 'show create table %s' % table)[0]['Create Table']
        primary_key = re.search(r'PRIMARY KEY \((.+)\)', create_sql).group(1).split(',')
        if len(primary_key) == 1 and primary_key[0].strip('`').lower() == 'id':
            primary_key = re.search(r'UNIQUE KEY [`\w]+ \((.+)\)', create_sql).group(1).split(',')
        primary_key = [k.strip('`') for k in primary_key]

        data = []
        sql = ""
        delete_where = list()
        if isinstance(result, list):
            for item in result:
                _check_user_params(item, primary_key)
                all_keys = [k for k in item.keys() if k not in ignore_columns]
                delete_where.append(' and '.join(['%s=%s' % (k, v) for k, v in item.items() if k in primary_key]))
                all_keys.sort()
                values = [item[i] for i in all_keys]
                data.append(tuple(values))
                if not sql:
                    keys = ', '.join(["%s=VALUES(%s)" % (k, k) for k in all_keys if k not in primary_key])
                    sql_keys = map(lambda x: '`%s`' % x, all_keys)
                    sql = "INSERT INTO %s (%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s" % (table,  ", ".join(sql_keys),
                                                        ", ".join(["%s" for _ in xrange(len(all_keys))]), keys)
        elif isinstance(result, dict):
            _check_user_params(result, primary_key)
            all_keys = [k for k in result.keys() if k not in ignore_columns]
            delete_where.append(' and '.join(['%s=%s' % (k, v) for k, v in result.items() if k in primary_key]))
            all_keys.sort()
            values = [result[i] for i in all_keys]
            data.append(tuple(values))
            if not sql:
                keys = ', '.join(["%s=VALUES(%s)" % (k, k) for k in all_keys if k not in primary_key])
                sql_keys = map(lambda x: '`%s`' % x, all_keys)
                sql = "INSERT INTO %s (%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s" % (table, ", ".join(sql_keys),
                                                        ", ".join(["%s" for _ in xrange(len(all_keys))]), keys)
        update_row_count = self.db_client[db].executemany_rowcount(sql, data)
        if not update_row_count:
            return 0, 0
        now = (datetime.datetime.now()-datetime.timedelta(minutes=expire_minute)).strftime("%Y-%m-%d %H:%M:%S")
        # delete
        delete_row_count = 0
        for d in delete_where:
            sql = 'DELETE FROM ' + table + ' WHERE ' + d + ' and `%s`<%s'
            delete_row_count += self.db_client[db].execute_rowcount(sql, update_time_column, now)
        return update_row_count, delete_row_count

    def write_db(self, db, table, result, insert_ignore=False):
        """Write data to db.
        """
        # build data.
        data = []
        sql = ""
        if isinstance(result, list):
            for item in result:
                keys = item.keys()
                keys.sort()
                values = [item[i] for i in keys]
                data.append(tuple(values))
                if not sql:
                    sql_keys = map(lambda x: '`%s`' % x, keys)
                    sql = "%s INTO %s (%s) VALUES (%s)" % ("INSERT IGNORE" if insert_ignore else "REPLACE",
                                                           table, ", ".join(sql_keys),
                                                           ", ".join(["%s" for i in xrange(len(keys))]))
        elif isinstance(result, dict):
            keys = result.keys()
            keys.sort()
            values = [result[i] for i in keys]
            data.append(tuple(values))
            if not sql:
                sql_keys = map(lambda x: '`%s`' % x, keys)
                sql = "%s INTO %s (%s) VALUES (%s)" % ("INSERT IGNORE" if insert_ignore else "REPLACE",
                                                       table, ", ".join(sql_keys),
                                                       ", ".join(["%s" for i in xrange(len(keys))]))
        # exec sql.
        return self.db_client[db].executemany_rowcount(sql, data)

    def write_db_with_update(self, db, table, result, get_rowcount=True):
        return self.write_db_wang(db, table, result, get_rowcount)

    # def delete_outdated_rows(self, db, table):

    def write_db_wang(self, db, table, result, get_rowcount=True):
        """Write data to db.
        """
        # build data.
        data = []
        sql = ""
        select_sql = ""
        select_keys = []
        select_data = []
        is_many = True
        if isinstance(result, list):
            for item in result:
                keys = item.keys()
                keys.sort()
                values = [item[i] for i in keys]
                data.append(tuple(values))
                if not sql:
                    sql_keys = map(lambda x: '`%s`' % x, keys)
                    sql = "INSERT INTO %s(%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s" % (table,
                                                                                         ", ".join(sql_keys),
                                                                                         ", ".join(["%s" for i in xrange(len(keys))]),
                                                                                         ", ".join(i+" = VALUES(%s)" % (i) for i in sql_keys if i != "`ip`"))
        elif isinstance(result, dict):
            is_many = False
            keys = result.keys()
            keys.sort()
            # values =
            data = [result[i] for i in keys]
            select_keys = [i for i in keys if result[i]]
            select_data = [result[i] for i in keys if result[i]]
            if not sql:
                sql_keys = map(lambda x: '`%s`' % x, keys)
                sql = "INSERT INTO %s(%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s" % (table,
                                                                                        ", ".join(sql_keys),
                                                                                        ", ".join(["%s" for i in xrange(len(keys))]),
                                                                                        ", ".join(i+" = VALUES(%s)" % (i) for i in sql_keys if i != "`ip`"))
            if not select_sql:
                select_sql = "select * from `%s` where " % table
                select_sql += " and ".join(["`%s` = %%s" % k for k in select_keys])
                # print select_sql
        # exec sql.
        db_client = None
        if isinstance(db, str):
            db_client = self.db_client[db]
        elif isinstance(db, Connection):
            db_client = db
        else:
            raise RuntimeError("Unsupported db argument type: %s" % db)
        if is_many:
            if get_rowcount:
                return db_client.executemany_rowcount(sql, data)
            else:
                return db_client.executemany_lastrowid(sql, data)
        else:
            if get_rowcount:
                return db_client.execute_rowcount(sql, *data)
            else:
                db_client.execute_lastrowid(sql, *data)
                return db_client.get(select_sql, *select_data)


    def write_to_db(self, table, result):
        """Write data to db.
        """
        if not self.db_name:
            raise RuntimeError("DB name is empty!")
        return self.write_db(self.db_name, table, result)

    @staticmethod
    def gen_uuid(data):
        """Gen uuid by data.
        """
        return md5.new(data).hexdigest()

    @staticmethod
    def static_logger(step_name, message):
        print "[base][%s]%s" % (step_name, message)

    def debug_logger(self, step_name, message):
        if self.debug:
            thread_name = threading.currentThread().getName(),
            step_name = "%s: %s" % (thread_name[0], step_name)
            self.logger.info(step_name, message)

    def thread_logger(self, step_name, message):
        thread_name = threading.currentThread().getName(),
        step_name = "%s: %s" % (thread_name[0], step_name)
        self.static_logger(step_name, message)

    def log_debug(self, message, step=None, is_print=False):
        self.logger.debug(message, step, is_print)

    def log_info(self, message, step=None, is_print=False):
        self.logger.info(message, step, is_print)

    def log_warn(self, message, step=None, is_print=False):
        self.logger.warn(message, step, is_print)

    def log_error(self, message, step=None, is_print=False):
        self.logger.error(message, step, is_print)


    '''
    远程执行etl sql（如"insert into XXX select XXX "类型的sql）
    '''

    def execute_etl_sql_remote(self, db, sql, retry=1, timeout=DEFAULT_ETL_TIMEOUT):
        success = False
        err_msg = ''
        job_status = ''
        for i in xrange(retry):
            remote_sql = "SUBMIT JOB " + sql
            job_info = self.db_client[db].get(remote_sql)
            job_id = job_info["job_id"]
            self.thread_logger("Submit remote sql", "Exec sql remotely start, database: %s, job_id: %s " % (db, job_id))
            self.debug_logger("Sql statement", remote_sql.replace("%%", "%"))

            begin_ts = arrow.Arrow.now()
            while True:
                job_status = self.query_job_status(db, job_id)
                if etl_db.is_job_running(job_status["status"]):
                    now_ts = arrow.Arrow.now()
                    time_cost = (now_ts - begin_ts).total_seconds()
                    if time_cost > timeout:
                        err_msg = 'Execute sql remote timeout'
                        self.thread_logger("Exec remote sql",
                                           "Exec sql remotely timeout! Database: %s, job id: %s, sql: %s" %
                                           (db, job_id, remote_sql))
                        break
                    time.sleep(etl_db.ASYNC_JOB_QUERY_INTERVAL)
                elif job_status["status"] == etl_db.ASYNC_JOB_FAILED:
                    self.thread_logger("Exec sql failed",
                                       "Job id: %s, reason: %s" % (job_status["job_id"], job_status["fail_msg"]))
                    self.debug_logger("Exec sql failed", "Details info: %s" % job_status)
                    err_msg = 'Execute sql remote failed'
                    break
                else:
                    self.thread_logger("Exec remote sql success",
                                       "Exec sql remotely success, database: %s, job_id: %s " % (db, job_id))
                    success = True
                    break
            if success:
                return
        else:
            raise OperationalError(err_msg)

    '''
        远程执行etl sql（如"insert into XXX select XXX "类型的sql）
        '''

    def execute_sql_remote(self, sql, db=None, timeout=DEFAULT_ETL_TIMEOUT):
        if not db:
            db = self.db_name
        self.execute_etl_sql_remote(db, sql, timeout)

    '''
        远程执行etl sql（如"insert into XXX select XXX "类型的sql）
        '''

    def execute_etl_sql(self, db, sql, table, timeout=DEFAULT_ETL_TIMEOUT):
        result = self.db_client[db].query(sql)
        if not result:
            return "No data from sql"
        self.write_db(db, table, result)

    def query_job_status(self, db, job_id):
        sql = "show job status where job=%s"
        return self.db_client[db].get(sql, job_id)

    def close_db_connection(self):
        for db_client in self.db_client.itervalues():
            db_client.close()

    def rebuild_db_connection(self, db=None):
        if db:
            self.db_client.pop(db)
            db_config = DB_CONFIG[db]
            self.db_client[db] = torndb.Connection(db_config["HOST"] + ":" + str(db_config["PORT"]),
                                                   db_config["DB"],
                                                   db_config["USER"],
                                                   db_config["PWD"],
                                                   time_zone='+8:00')
        else:
            self.__init_db()

    # @thread_timeout(seconds=60, rebuild_db_connection=True)
    def query(self, sql, db=None):
        if not db:
            return self.db_client[self.db_name].query(sql)
        return self.db_client[db].query(sql)

    # @thread_timeout(seconds=60, rebuild_db_connection=True)
    def get(self, sql, db=None):
        if not db:
            return self.db_client[self.db_name].get(sql)
        return self.db_client[db].get(sql)

    # @thread_timeout(seconds=60, rebuild_db_connection=True)
    def execute(self, sql, db=None):
        if not db:
            return self.db_client[self.db_name].execute(sql)
        return self.db_client[db].execute(sql)

    def execute_p(self, db, sql, *parameters, **kwparameters):
        return self.db_client[db].execute_rowcount(sql, *parameters, **kwparameters)

    def update_p(self, db, sql, *parameters, **kwparameters):
        return self.db_client[db].update(sql, *parameters, **kwparameters)

    def updatemany_p(self, db, sql, *parameters):
        return self.db_client[db].updatemany(sql, *parameters)

    def insert_p(self, db, sql, *parameters, **kwparameters):
        return self.db_client[db].insert(sql, *parameters, **kwparameters)

    def insertmany_p(self, db, sql, *parameters):
        return self.db_client[db].insertmany(sql, *parameters)

    def query_p(self, db, sql, *parameters, **kwparameters):
        return self.db_client[db].query(sql, *parameters, **kwparameters)

    def get_p(self, db, sql, *parameters, **kwparameters):
        return self.db_client[db].get(sql, *parameters, **kwparameters)

    def executemany_p(self, db, sql, *parameters):
        return self.db_client[db].executemany(sql, *parameters)

    def execute_rowcount(self, db, sql, *parameters):
        return self.db_client[db].execute_rowcount(sql, *parameters)

    @process_timeout()
    def query_with_timeout(self, sql, timeout=30, db=None):
        if not db:
            return self.db_client[self.db_name].query(sql)
        return self.db_client[db].query(sql)

    @process_timeout()
    def get_with_timeout(self, sql, timeout=30, db=None):
        if not db:
            return self.db_client[self.db_name].get(sql)
        return self.db_client[db].get(sql)

    @process_timeout()
    def execute_with_timeout(self, sql, timeout=30, db=None):
        if not db:
            return self.db_client[self.db_name].execute(sql)
        return self.db_client[db].execute(sql)

    get_new_client = get_new_db_client
    get_local = get
