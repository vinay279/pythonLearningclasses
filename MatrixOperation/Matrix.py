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
            return matrix

    def matrixADD(self,matrix1, matrix2):
        Z = []
        for i in range(0, len(matrix1)):
            for column in range(0, len(matrix1)):
                result = matrix1[i][column] + matrix2[i][column]
                Z[i][column] = (result)
                Z([i][column]) + 1
        return Z



c = MatrixOperation()
matrix1=c.creatematrix()
matrix2= c.creatematrix()
c.matrixADD(matrix1,matrix2)
