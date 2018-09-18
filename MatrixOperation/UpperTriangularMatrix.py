''' class for the upper triangular matrix '''
from MatrixOperation.MatrixCreation import CreateNullMAtrix as K
class UpperTriangularMatrix:

    def upperTriangularMatrix(self):

        for row in range(0, len(K.Matrix)):
            for col in range(0, len(K.Matrix[0])):
                if row >= col:
                    K.Matrix[row][col] = int(input("Enter the values you want enter in the Upper triangular Matrix = "))
                else:
                    K.Matrix[row][col] = 0
        print("\n")
        print(" Upper Triangular Matrix :")
        for values in K.Matrix:
            print(values)



objz = UpperTriangularMatrix()
objz.upperTriangularMatrix()
