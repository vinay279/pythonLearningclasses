''' class for the genration of identity matrix

 Identity Matrix: It is a type of square matrix which
 has all the main diagonal elements equal to 1 and all t
 he non-diagonal elements equal to 0. It is also called unit matrix.

Example of unit matrix can be given as = | 1  0  0 |
                                         | 0  1  0 |
                                         | 0  0  1 |
'''
from MatrixOperation.MatrixCreation import CreateNullMAtrix as M
class IdentityMatrix:

    def identityMatrix(self):
        if len(M.Matrix) == len(M.Matrix[0]):
            for row in range(0, len(M.Matrix)):
                for col in range(0, len(M.Matrix[0])):
                    if row == col:
                        M.Matrix[row][col] = 1
                    else:
                        M.Matrix[row][col] = 0


            print(" Now the Identity Matrix is created  :")
            for values in M.Matrix:
                print(values)

cl = IdentityMatrix()
cl.identityMatrix()
