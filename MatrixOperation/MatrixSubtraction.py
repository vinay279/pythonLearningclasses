''' class for the matrix addition '''

class MatrixSubtraction:
    def matrixSubtraction(self):

        #Prints the sum of matrix of orders mxn
        first_row_count = int(input('Enter the number of rows of 1st matrix :'))
        first_col_count = int(input('Enter the number of columns of 1st matrix :'))

        second_row_count = int(input('Enter the number of rows of 2nd matrix :'))
        second_col_count = int(input('Enter the number of columns of 2nd matrix :'))

        first_Matrix = []
        second_matrix = []

        if(first_row_count == second_row_count) and (second_row_count == second_col_count):
            print('Enter the elements of first Matrix')
            for irow in range(0, first_row_count):
                row = []

                for jcol in range(0, first_col_count):
                    input_variable = int(input('Enter the element at mat[{0}][{1}]'.format(irow, jcol,'\n')))
                    row.append(input_variable)
                first_Matrix.append(row)
            print(first_Matrix,'\n')

            print('Enter the elements of second Matrix')
            for irow in range(0, second_row_count):
                row = []

                for jcol in range(0, second_col_count):
                    input_variable = int(input('Enter the element at mat[{0}][{1}]'.format(irow, jcol)))
                    row.append(input_variable)
                second_matrix.append(row)
            print("Second Matrix", second_matrix)


            print(' Matrix Output')
            result = []
            for resultrows in range(0, first_row_count):
                result.append([])

            for row in range(0, first_col_count):
                for col in range(0, second_row_count):
                    result[row].append(col)
                    result[row][col] = 0

            if first_row_count == second_row_count == first_col_count==second_col_count:
                for rowinmat1 in range(0, len(first_Matrix)):
                    for roweleM2of0 in range(0, len(second_matrix[0])):
                        for rowsinm2 in range(0, len(second_matrix)):
                            result[rowinmat1][roweleM2of0] = first_Matrix[rowinmat1][rowsinm2] - second_matrix[rowsinm2][roweleM2of0]
            print("matrix Output")
            for values in result:
                   print(values)
        else:
            print('The  Size of matrix are differnt ')
        print('The Matrix Sum performed')
q = MatrixSubtraction()
q.matrixSubtraction()
