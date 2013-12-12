#import sys
#print('\n'.join(sorted(sys.path)))
import re
import csv

_file = open('stockdata','r+')
_decode = open('decodedata', 'w+')

'''for line in _file.readlines():
    line.decode('gb2312').encode('utf8')
    _decode.write(line)'''
reader = csv.reader(open("stockdata"), delimiter="\t")

buy = '\xc3\x82\xc3\xb2\xc3\x85\xc3\x8c'
sell = '\xc3\x82\xc3\xb4\xc3\x85\xc3\x8c'
neutral = '\xc3\x96\xc3\x90\xc3\x90\xc3\x94\xc3\x85\xc3\x8c'

#for v1,v2,v3,v4,v5,v6 in reader:
#    print '%r %r'%(v1,v6)

for v1,v2,v3,v4,v5,v6 in reader:
    if reader.line_num == 1:
        continue
    if v6 == buy:
        print 'buy'
    elif v6 == sell:
        print 'sell'
    elif v6 == neutral:
        print 'neutral'
    else:
        print 'error'
        
_file.close()
_decode.close()


    