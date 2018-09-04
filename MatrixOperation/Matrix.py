'''This class is used for the matrix operation add,divide,subtract and multiplication'''

class MatrixOperation:

    def creatematrix(self):
            rows = int(input("Enter number of rows in the matrix: "))
            columns = int(input("Enter number of columns in the matrix: "))
            matrix = []
            print("Enter the %s x %s matrix: " % (rows, columns))
            for i in range(rows):
                matrix.append(list(map(int, input().rstrip().split())))
            print("matrix created successflly")

    # method for the matrix multiplication
    def Mmultiplication(self,matrix1,matrix2):
            MatrixOperation.creatematrix()
            MatrixOperation.creatematrix()


c= MatrixOperation()
c.Mmultiplication()
