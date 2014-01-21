def ConvertStringToInt(istr):
    if istr.find(',') > 0:
        istr = istr.split(',')
        istr = ''.join(istr)
    
    if len(istr) > 10:
        return long(istr)
    else:
        return int(istr)
    
def MD5(istr):
    if not isinstance(istr, str):
        print 'MD5 function need an input string!'
        return ''
    import hashlib
    m = hashlib.md5()
    m.update(istr)
    return m.hexdigest()