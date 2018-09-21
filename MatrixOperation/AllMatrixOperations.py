'''                      class for the all matrix Operation
1] Addition   2] Subtraction   3]Multiplication    4] Create Identity Matrix    5] Diagonal/Scalar Matrix
6] Lower Triangular Matrix   7] Upper Triangular Matrix   8] Create Square matrix   9] Create Null Matrix   '''
class MatrixOperations:

    # for Printing values from matrix
    def printValuesfromMat(self, mat):
        for values in mat:
            print(values)

    # create and enter values in Square matrix
    def enterSquareMatrix(self):
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
        self.printValuesfromMat(Matrix)
        return Matrix

    # create Square matrix with zero values
    def createSqureMatWithZero(self):
        print('Enter Square matrix value for operation\n'
              'For Ex - for [2 Rows * 2 Columns] matrix Enter = 2\n'
              '         for [3 Rows * 3 Columns] matrix Enter = 3\n')
        matrixrow = int(input())
        mat = []
        for rowsinm1 in range(0, matrixrow):
            mat.append([])

        for row in range(0, matrixrow):
            for col in range(0, matrixrow):
                mat[row].append(col)
                mat[row][col] = 0
        return mat

    # for getting input rows and column and enter values
    def enterMatrix(self):
        rowINM1 = int(input('Enter the number of rows  :'))
        colInM1 = int(input('Enter the number of column :'))
        mat = []
        for rowsinm1 in range(0, rowINM1):
            mat.append([])
        print('Enter the elements of Matrix')
        for row in range(0, rowINM1):
            for col in range(0, colInM1):
                mat[row].append(col)
                mat[row][col] = 0
                mat[row][col] = int(input('-row {0} col {1} ='.format(row, col, '\n')))
        self.printValuesfromMat(mat)
        return mat

    # for matrix Addition
    def matrixAddition(self):
        print("****  Matrix Addition  *****")
        Matrix1 = self.enterSquareMatrix()
        print("For second Matrix")
        Matrix2 = self.enterSquareMatrix()
        if len(Matrix1) == len(Matrix2):
            for rowinfst in range(0, len(Matrix1)):
                for col in range(0, len(Matrix1[0])):
                    Matrix1[rowinfst][col] = Matrix1[rowinfst][col] + Matrix2[rowinfst][col]
            print("Matrix Addition in Output matrix is ")
            self.printValuesfromMat(Matrix1)
            print("Matrix Addition is performed")
            Matrix1.clear()

    # for Subtraction
    def matrixSubtraction(self):
        print('***  Matrix Subtraction  ***')
        Matrix1 = self.enterSquareMatrix()
        print("For second Matrix")
        Matrix2 = self.enterSquareMatrix()
        if len(Matrix1) == len(Matrix2):
            for rowinfst in range(0, len(Matrix1)):
                for col in range(0, len(Matrix1[0])):
                    Matrix1[rowinfst][col] = Matrix1[rowinfst][col] - Matrix2[rowinfst][col]
            print("Matrix Subtraction in Output matrix is ")
            self.printValuesfromMat(Matrix1)
            print("Matrix Subtraction is performed")
            Matrix1.clear()

    # method for matrix multiplication
    def MatrixMultiplication(self):
        print('***  Matrix Multiplication  ***')
        print('NOTE- In the Matrix multiplication '
              'Number of Columns in 1st Matrix should = Rows 2nd Matrix'
              'And result will be no of rows from first and column from 2nd')
        print('For 1st Matrix')
        mat1 = self.enterMatrix()
        print('For Second Matrix')
        mat2 = self.enterMatrix()
        result = []
        for rowsinresult in range(len(mat1)):
            result.append([])
        for row in range(0, len(mat1)):
            for col in range(0, len(mat2[0])):
                result[row].append(col)
                result[row][col] = 0
        if len(mat1[0]) == len(mat2):
            for rowinmat1 in range(0, len(mat1)):  # until rows in mat1
                for colinm2 in range(0, len(mat2[0])):  # until columns in mat2
                    for rowsinm2 in range(0, len(mat2)):  # until rows in mat2
                        result[rowinmat1][colinm2] += mat1[rowinmat1][rowsinm2] * mat2[rowsinm2][colinm2]

            print('Matrix multiplication Output')
            self.printValuesfromMat(result)
        else:
            print("please provide proper input")

    # create transpose Matrix
    def transposeMatrix(self):
        print('*****Transpoe Matrix Operation*****')
        Mat = self.enterMatrix()
        result = []
        for colinresult in range(0, len(Mat[0])):
            result.append([])
        for col in range(0, len(Mat)):
            for row in range(0, len(Mat[0])):
                result[row].append(col)

        for row in range(len(Mat)):
            # iterate through columns
            for col in range(len(Mat[0])):
                result[col][row] = Mat[row][col]  # INTERCHANGING THE COLUMN IN ROWS
        print("The Transposed of given Matrix is :")
        self.printValuesfromMat(result)

    # create Indentity Matrix
    def createIdentityMatrix(self):
        print('*****Identity Matrix Operation*****')
        mat = self.createSqureMatWithZero()
        #####for identity
        for row in range(0, len(mat)):
            for col in range(0, len(mat[0])):
                if row == col:
                    mat[row][col] = 1
                else:
                    mat[row][col] = 0
        print("The Transposed of given Matrix is :")
        self.printValuesfromMat(mat)

    # create Diagonal matrix
    def createDiagonalMatrix(self):
        print('*****Diagonal Matrix Operation*****')
        mat = self.createSqureMatWithZero()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row == col:
                    mat[row][col] = int(input("Enter the values you want enter diagonally "))
                else:
                    mat[row][col] = 0
        print("The Transposed of given Matrix is :")
        self.printValuesfromMat(mat)

    # create Lower triangular matrix
    def lowerTriangularMat(self):
        Mat = self.createSqureMatWithZero()
        for row in range(0, len(Mat)):
            for col in range(0, len(Mat[0])):
                if row <= col:
                    Mat[row][col] = int(input("Enter the value in Lower triangular Matrix "))
                else:
                    Mat[row][col] = 0
        print("Lower Triangular Matrix Output :")
        self.printValuesfromMat(Mat)

    def upperTriangularMat(self):
        Matrix = self.createSqureMatWithZero()
        for row in range(0, len(Matrix)):
            for col in range(0, len(Matrix[0])):
                if row <= col:
                    Matrix[row][col] = int(input("Enter the value in Upper triangular Matrix "))
                else:
                    Matrix[row][col] = 0
        print("Upper Triangular Matrix Output is :")
        self.printValuesfromMat(Matrix)






