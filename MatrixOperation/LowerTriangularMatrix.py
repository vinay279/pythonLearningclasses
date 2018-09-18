''' class for the Lower Triangular Matrix '''
from MatrixOperation.MatrixCreation import Create as K
class LowerTriangularMatrix:
    def lowerTriangularMatrix(self):

        for row in range(0, len(K.Matrix)):
            for col in range(0, len(K.Matrix[0])):
                if row <= col:
                    K.Matrix[row][col] = int(input("Enter the values you want enter in the Lower triangular Matrix "))
                else:
                    K.Matrix[row][col] = 0

        print("\n")
        print("Lower Triangular Matrix  :")
        for values in K.Matrix:
            print(values)


z= LowerTriangularMatrix()
z.lowerTriangularMatrix()

