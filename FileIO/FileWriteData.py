'''this class is for writing data '''
from builtins import print


class FIleIO:
    def __init__(self,filename):
        self.filename = filename

    def FileOpen(self,filename):
        while True:
            print(" Select Option you want to perform \n"
                    "1.create file\n"
                    "2.write data to file\n"
                    "3.Edit the file content\n")
            menu = int(input("select any option you want to perform"))
            if menu == 1:
                           f = open(input(input("enter the "), 'r')
                f.write("this is the python file #we can write in string")
                f.write("my file program")
                f.write("my io operatiion")
                list =['c\n','java\n', 'didi\n', '2\n']
                f.writelines(list)
                print('data is written successfully')
                f.read()#to read total data
                f.readline(1)#to read any single line
                f.read(200)#for reading the charactors from file