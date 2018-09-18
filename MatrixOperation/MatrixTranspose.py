''' class doing transpose Matrix Operation

    Matrix Transpose - In the transpose matrix we change the number of column into rows

    Example of Transpose matrix 4*3 can be given as =     | 1  0  0 |
                                                          | 0  1  0 |
                                                          | 0  0  1 |
                                                          | 0  0  1 |

    Output Transpose Matrix will be 3 * 4  matrix ==
                                                          | 1  0  0  0 |
                                                          | 0  1  0  0 |
                                                          | 0  0  1  1 |

    '''


class TransposeMatrix:

    def transposeMatrix(self):
        # taking user input
        rowINM = int(input("Enter the Numbers of Rows ="))
        colsInM = int(input("Enter the Numbers of Column ="))

        # Empty  matrix
        Matrix = []

        for rowsinmat in range(0, rowINM):
            Matrix.append([])   # Appending rows to the matrix

        print('Enter the elements of first Matrix')
        for row in range(0, rowINM):
            for col in range(0, colsInM):
                Matrix[row].append(col)
                Matrix[row][col] = 0
                print('row', row + 1, 'col', col + 1)
                Matrix[row][col] = int(input())
        print("The Matrix you Entered :")
        for values in Matrix:
            print(values)

        # CREATING THE RESULT MATRIX
        result = []
        for colinresult in range(0,colsInM):
            result.append([])
        for col in range(0, rowINM):
            for row in range(0, colsInM):
                result[row].append(col)
                result[row][col] = 0  # appending zeros to the result matrix


        for row in range(len(Matrix)):
            # iterate through columns
            for col in range(len(Matrix[0])):
                result[col][row] = Matrix[row][col]     # INTERCHANGING THE COLUMN IN ROWS
        print("The Transposed of given Matrix is :")
        for values in result:
            print(values)


t = TransposeMatrix()
t.transposeMatrix()