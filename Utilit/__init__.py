def ConvertStringToInt(istr):
    if istr.find(',') > 0:
        istr = istr.split(',')
        istr = ''.join(istr)
    
    if len(istr) > 10:
        return long(istr)
    else:
        return int(istr)