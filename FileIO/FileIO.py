''' This class is used for the creation FileIO operations '''
import os
class FileIO:

    # this method is use for creating the file
    def createfile(self):
        try:
            open(input("Enter file name You want to give ")+".txt", 'x')
            print('File created successfully')
        except FileExistsError:
            print("file already present please give another name ")

    # This method is used for the read operation
    def readDataFromFile(self):
        f = open(input("Enter file name You want to give ") + ".txt", 'r')
        contents = f.read()
        print(contents)

    # This method is used for delete all previous data  write data to file
    def DeletePreviousAllAndwriteData2File(self):
        fh = open(input(" Enter the file name in which you want to write data "), "w")
        fh.write(input("Enter the data you want to write in file"))
        print("Data Written successfuly in file")
        fh.close()

    # METHOD for append data to existing file

    def AppendData2File(self):
        fh = open(input("Enter file name You want to give ")+".txt",  "+a")
        fh.write(input("Enter data you want to append in the file "))
        fh.close

    # Method for delete all data from file

    def deleteDataFromFile(self):
        open(input("Enter Filename you want to Delete all data from that"), 'w').close()

    # MEthod for Rename the file
    def renameFile(self):

        os.rename(input("Enter FileName"), input("Enter NewFileName"))

    # method for calling all methods of class
    def callingFIO(self):
        c = FileIO()
        while True:
            print("1.Create File\n"
                  "2.Read Data from File\n"
                  "3.Append Data to File\n"
                  "4.Delete All Data from File\n"
                  "5.Rename File")
            press = int(input("*********Select the operation you want**************"))

            if press == 1:
                c.createfile()

            elif press == 2:
                c.readDataFromFile()

            elif press ==3:
                c.AppendData2File()

            elif press == 4:
                c.deleteDataFromFile()

            elif press == 5:
                c.renameFile()



