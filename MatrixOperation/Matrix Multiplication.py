class MatrixMultiplication:
    def matrixmul(self):
        print('MATRIX MULTIPLICATION\n')

        # Ask user for dimensions of first matrix
        rows = int(input("Matrix1: Number of rows?: "))
        column = int(input("Matrix1: Number of columns?: "))

        # Print design of first Matrix for better understanding of elements' naming convention
        print('''\nElements of matrix1:''')
        element = ''  # Later will be used to construct each row of the matrix
        for vrow in range(0, rows):  # vr - variable row
            for vc in range(0, column):  # vc - variable column
                element += 'M' + str(vrow + 1) + str(vc + 1) + ' '
            print('|', element, '\b|')
            element = ''

        # Create empty Matrix1 and fill it with user input element by element
        Matrix1 = [[] for vrow in range(0, rows)]
        for vr in range(0, rows):
            Matrix1[vr] = [0 for vc in range(0, column)]

        for vr in range(0, rows):
            for vc in range(0, column):
                Matrix1[vrow][vc] = int(input('M' + str(vrow + 1) + str(
                    vc + 1) + ': '))  # + 1 because vr and vc starts at 0 and we want elements be named from 1

        # Ask the user for dimension of second matrix
        col2 = int(input("Matrix2: Number of columns?: "))  # Only for columns since M2 rows = M1 columns by definition
        print('''\nElements of matrix Matrix2:''')
        element = ''
        for vr in range(0, column):  # vr in c because Matrix 2 must have the same number of rows as Matrix1 columns.
            for vc in range(0, col2):
                element += 'M' + str(vrow + 1) + str(vc + 1) + ' '
            print('|', element, '\b|')
            element = ''

        # Create Empty Matrix2 and fill it with user input element by element
        Matrix2 = [[] for vrow in range(0, column)]
        for vrow in range(0, column):
            Matrix2[vrow] = [0 for vc in range(0, col2)]

        for vrow in range(0, column):
            for vc in range(0, col2):
                Matrix2[vrow][vc] = int(input('M' + str(vrow + 1) + str(vc + 1) + ': '))

        # Create empty Product Matrix for Result of multiplication of Matrix1 and Matrix2
        Product = [[] for vrow in range(0, rows)]  # Number of rows defined by number of rows in Matrix1
        for vrow in range(0, rows):
            Product[vrow] = [0 for columns in range(col2)]  # Number of columns defined by number of columns in Matrix2

        # Calculate the Product of two tables
        Products = 0  # dummy variable for calculating sum of product of each row and column
        for vv in range(0, col2):
            for vrow in range(0, rows):
                for vc in range(0, column):
                    Products += Matrix1[vrow][vc] * Matrix2[vc][vv]
                Product[vrow][vv] = Products
                Products = 0  # clear the variable when looped for whole column of Matrix2

        print('Matrix1: ', Matrix1)
        print('Matrix2: ', Matrix2)
        print('Result of Matrix Multiplication:', Product)

        input('Press "Enter" to Exit')