# writing data to file

f=open('abc.txt', 'r')
f.write("this is the python file #we can write in string")
f.write("my file program")
f.write("my io operatiion")
list=['c\n','java\n', 'didi\n', '2\n']
f.writelines(list)
print('data is written successfully')
f.read()#to read total data
f.readline(1)#to read any single line
f.read(200)#for reading the charactors from file