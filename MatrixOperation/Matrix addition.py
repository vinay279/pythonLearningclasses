''' class for the matrix addition '''

class MatrixAddition:
    def matrixAddition(self):

        #Prints the sum of matrix of orders mxn
        first_row_count = int(input('Enter the number of rows of 1st matrix :'))
        first_col_count = int(input('Enter the number of columns of 1st matrix :'))

        second_row_count = int(input('Enter the number of rows of 1st matrix :'))
        second_col_count = int(input('Enter the number of columns of 1st matrix :'))

        first_Matrix = []
        second_matrix = []

        if(first_row_count == second_row_count) and (second_row_count == second_col_count):
            print('Enter the elements of first Matrix')
            for irow in range(0, first_row_count):
                row = []

                for jcol in range(0, first_col_count):
                    input_variable = int(input('Enter the element at mat[{0}][{1}]'.format(irow, jcol)))
                    row.append(input_variable)
                first_Matrix.append(row)

            print('Enter the elements of second Matrix')
            for irow in range(0, second_row_count):
                row = []

                for jcol in range(0, second_col_count):
                    input_variable = int(input('Enter the element at mat[{0}][{1}]'.format(irow, jcol)))
                    row.append(input_variable)
                second_matrix.append(row)


            print(' Matrix Output')
            result = [[first_Matrix[index][jindex] + second_matrix[index][jindex]
                       for jindex in range(len(first_Matrix[0]))]
                         for index in range(len(first_Matrix))]
            for values in result:
                   print(values)
        else:
            print('The  Size of matrix are differnt ')
        print('The Matrix Sum performed')
q = MatrixAddition()
q.matrixAddition()
