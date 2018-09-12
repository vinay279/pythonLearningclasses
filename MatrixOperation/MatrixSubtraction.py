''' class for the matrix Subtraction '''

class MatrixSubtraction:
    def matrixSubtraction(self):

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
                input_variable = None
                for jcol in range(0, first_col_count):
                    input_variable = int(input('Enter the element at mat[{0}][{1}]'.format(irow, jcol)))
                    row.append(input_variable)
                first_Matrix.append(row)

            print('Enter the elements of second Matrix')
            for irow in range(0,second_row_count):
                row = []
                input_variable = None
                for jcol in range(0,second_col_count):
                    input_variable = int(input('Enter the element at mat[{0}][{1}]'.format(irow, jcol)))
                    row.append(input_variable)
                second_matrix.append(row)

            print('Resultant Matrix')
            Subtraction = [[first_Matrix[irow][jcol] - second_matrix[irow][jcol]
                       for jcol in range(len(first_Matrix[0]))]
                      for irow in range(len(first_Matrix))]
            for result in Subtraction:
                   print(result)
        else:
            print('The Size of matrix are Diffrent')
        print('The Matrix Subtraction  performed')
q= MatrixSubtraction()
q.matrixSubtraction()
