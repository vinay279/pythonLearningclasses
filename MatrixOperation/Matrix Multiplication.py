class MatrixMultiplication:
    print('MATRIX MULTIPLICATION\n')
    print("NOTE - The 1st MATRIX COLUMNS COUNT = 2ND MATRIX ROWS COUNT")

    # Prints the sum of matrix of orders mxn
    first_row_count = int(input('Enter the number of rows of 1st matrix :'))
    first_col_count = int(input('Enter the number of columns of 1st matrix :'))

    second_row_count = int(input('Enter the number of rows of 2nd matrix :'))
    second_col_count = int(input('Enter the number of columns 2nd 1st matrix :'))

    first_Matrix = []
    second_matrix = []
    if first_col_count == second_row_count:

        print('Enter the elements of first Matrix')
        for rowValue1 in range(0, first_row_count):
            M1Row = []

            for colValue1 in range(0, first_col_count):
                input_variable = int(input('Enter the element at matrix[{0}][{1}]'.format(rowValue1, colValue1)))
                M1Row.append(input_variable)
            first_Matrix.append(M1Row)

        print('Enter the elements of first Matrix')
        for rowValue2 in range(0, first_row_count):
            M2row = []

            for j in range(0, first_col_count):
                input_variable = int(input('Enter the element at matrix[{0}][{1}]'.format(rowValue2, j)))
                M2row.append(input_variable)
            second_matrix.append(M2row)


            print('Matrix output')
            result = [[first_Matrix[i][j] * second_matrix[j][i]
                       for j in range(len(first_Matrix[0]))]
                      for i in range(len(first_Matrix))]

            for values in result:
                print(values)
        else:
            print('The  Size of matrix are differnt ')
        print('The Matrix Sum performed')