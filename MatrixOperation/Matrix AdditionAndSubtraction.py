''' class for the matrix addition '''
from
class MatrixOperations:
    # method for Accepting user input in matrix
    def enterMatrix(self):
        print('Enter Square matrix value for operation\n'
                              'For Ex - for 2*2 matrix Enter = 2\n'
                              '         for 3*3 matrix Enter = 3\n')
        matrixrow = int(input())
        print("Enter The Values Of Matrix")
        Matrix = []
        for rowsInMatrix in range(0, matrixrow):
            Matrix.append([])

        for row in range(0, matrixrow):
            for col in range(0, matrixrow):
                Matrix[row].append(col)
                Matrix[row][col] = 0
                Matrix[row][col] = int(input('-row {0} col {1} ='.format(row, col, '\n')))
        for values in Matrix:
            print(values)
        print("\n")
        return Matrix


    def matrixAddition(self):
        Matrix1 = self.enterMatrix()
        print("For second Matrix")
        Matrix2 = self.enterMatrix()
        if len(Matrix1) == len(Matrix2):
            for rowinfst in range(0, len(Matrix1)):
                for col in range(0, len(Matrix1[0])):
                    Matrix1[rowinfst][col] = Matrix1[rowinfst][col] + Matrix2[rowinfst][col]
            print("Matrix Addition in Output matrix is ")
            for values in Matrix1:
                    print(values)
            print("Matrix Addition is performed")
            Matrix1.clear()


    def matrixSubtraction(self):
        Matrix1 = self.enterMatrix()
        print("For second Matrix")
        Matrix2 = self.enterMatrix()
        if len(Matrix1) == len(Matrix2):
            for rowinfst in range(0, len(Matrix1)):
                for col in range(0, len(Matrix1[0])):
                    Matrix1[rowinfst][col] = Matrix1[rowinfst][col] - Matrix2[rowinfst][col]
            print("Matrix Subtraction in Output matrix is ")
            for values in Matrix1:
                print(values)
            print("Matrix Subtraction is performed")
            Matrix1.clear()

    def MatrixMultiplication(self):
        matrix

q = MatrixOperations()
q.matrixSubtraction()
