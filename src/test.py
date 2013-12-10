'''import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='root',
                     passwd='admin',
                     db='MyStock')

cur = db.cursor()

cur.execute('select * from stock_crawl_management')

for row in cur.fetchall():
    print row'''    

