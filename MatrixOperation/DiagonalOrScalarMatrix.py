''' class used for the creation of the diagonal matrix
        diagonal and scalar matrix are of the same type having all non diagonal
        values = 0

        ** Example f diagonal matrix  = | 1  0  0 |
                                        | 0  2  0 |
                                        | 0  0  3 |
        '''

class DiagonalMatrix:

    # method for creating the diagonal matrix
    def diagonalMatrix(self):

        for row in range(len(Matrix)):
            for col in range(len(Matrix[0])):
                if row == col:
                    Matrix[row][col] = int(input("Enter the values you want enter diagonally "))
                else:
                    Matrix[row][col] = 0

        print("\n")
        print("Diagonal Matrix  :")
        for values in Matrix:
            print(values)



s = DiagonalMatrix()
s.diagonalMatrix()