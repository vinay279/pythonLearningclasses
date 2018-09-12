class MatrixMultiplication:
    print('MATRIX MULTIPLICATION\n')
    print("NOTE - The 1st MATRIX COLUMNS COUNT = 2ND MATRIX ROWS COUNT")

    # Prints the sum of matrix of orders mxn
    first_row_count = int(input('Enter the number of rows of 1st matrix :'))
    first_col_count = int(input('Enter the number of columns of 1st matrix :'))

    second_row_count = int(input('Enter the number of rows of 1st matrix :'))
    second_col_count = int(input('Enter the number of columns of 1st matrix :'))

    first_Matrix = []
    second_matrix = []
    if first_col_count == second_row_count:

        print('Enter the elements of first Matrix')
        for rowValue1 in range(0, first_row_count):
            M1Rows = []
            input_variable = None
            for colValue1 in range(0, first_col_count):
                input_variable = int(input('Enter the element at mat[{0}][{1}]'.format(rowValue1, colValue1)))
                M1Rows.append(input_variable)
            first_Matrix.append(M1Rows)

        print('Enter the elements of first Matrix')
        for rowValue2 in range(0, first_row_count):
            row = []
            input_variable = None
            for j in range(0, first_col_count):
                input_variable = int(input('Enter the element at mat[{0}][{1}]'.format(rowValue2, j)))
                row.append(input_variable)
            second_matrix.append(row)

        resultMultiplication = []
        resultMultiplication = [first_Matrix[rowValue1][colValue1] * second_matrix[colValue1]]









    print('MATRIX MULTIPLICATION\n')

    # Ask user for dimensions of first matrix
    rows = int(input("Matrix1: Number of rows?: "))
    colM1 = int(input("Matrix1: Number of columns?: "))
    # Print first Matrix
    print('''\nElements of matrix1:''')
    element = ''  # Later will be used to construct each row of the matrix
    for vr in range(0, rows):  # vr - variable row
        for vc in range(0, colM1):  # vc - variable column
            element += 'M' + str(vr + 1) + str(vc + 1) + ' '
        print('|', element, '\b|')
        element = ''

    # Create empty Matrix1 and fill it with user input element by element
    Matrix1 = [[] for vr in range(0, rows)]
    for vr in range(0, rows):
        Matrix1[vr] = [0 for vc in range(0, colM1)]

    for vr in range(0, rows):
        for vc in range(0, colM1):
            Matrix1[vr][vc] = int(input('M' + str(vr + 1) + str(
                vc + 1) + ': '))  # + 1 because vr and vc starts at 0 and we want elements be named from 1

    # Ask the user for dimension of second matrix
    rowM2 = int(input("Matrix2: Number of columns?: ")) # Only for columns since M2 rows = M1 columns by definition

    print('''\nElements of matrix Matrix2:''')
    element = ''
    for vr in range(0, colM1):  # vr in c because Matrix 2 must have the same number of rows as Matrix1 columns.
        for vc in range(0, rowM2):
            element += 'M' + str(vr + 1) + str(vc + 1) + ' '
        print('|', element, '\b|')
        element = ''

    # Create Empty Matrix2 and fill it with user input element by element
    Matrix2 = [[] for vr in range(0, colM1)]
    for vr in range(0, colM1):
        Matrix2[vr] = [0 for vc in range(0, rowM2)]

    for vr in range(0, colM1):
        for vc in range(0, rowM2):
            Matrix2[vr][vc] = int(input('M' + str(vr + 1) + str(vc + 1) + ': '))

    # Create empty Product Matrix for Result of multiplication of Matrix1 and Matrix2
    Product = [[] for vr in range(0, rows)]  # Number of rows defined by number of rows in Matrix1
    for vr in range(0, rows):
        Product[vr] = [0 for columns in range(rowM2)]  # Number of columns defined by number of columns in Matrix2

    # Calculate the Product of two tables
    Products = 0  # dummy variable for calculating sum of product of each row and column
    for vv in range(0, rowM2):
        for vr in range(0, rows):
            for vc in range(0, colM1):
                Products += Matrix1[vr][vc] * Matrix2[vc][vv]
            Product[vr][vv] = Products
            Products = 0  # clear the variable when looped for whole column of Matrix2

    print('Matrix1: ', Matrix1)
    print('Matrix2: ', Matrix2)
    print('Result of Matrix Multiplication:', Product)

    # Footnotes
    print('\n\nCreated by: MK')
    input('Press "Enter" to Exit')