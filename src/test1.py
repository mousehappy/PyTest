import platform

print platform.architecture()


a = {'wsz':1, 'wsz2':2}

b = a

b['wsz3'] = 3
b['wsz'] = 4

print a.get('wsz')
print 5+int(a.get('111'))