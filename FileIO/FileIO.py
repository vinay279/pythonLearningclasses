
#Reading data from file
f=open('abc.txt', 'w')
print('file name', f.name)
print('is file is readable', f.readable())
print('file is writable or not', f.writable())
print('mode of file', f.mode)
print('is file is closed ', f.closed)


f.close()

