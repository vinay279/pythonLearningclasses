''' class for the matrix addition '''
import MatrixOperation
class MatrixSubtraction:
    def matrixSubtraction(self):
        Matrix1 = self.enterMatrix()
        print("For second Matrix")
        Matrix2 = self.enterMatrix()
        if len(Matrix1) == len(Matrix2):
            for rowinfst in range(0, len(Matrix1)):
                for col in range(0, len(Matrix1[0])):
                    Matrix1[rowinfst][col] = Matrix1[rowinfst][col] - Matrix2[rowinfst][col]
            print("Matrix Subtraction in Output matrix is ")
            for values in Matrix1:
                print(values)
            print("Matrix Subtraction is performed")
            Matrix1.clear()




q = MatrixSubtraction()
q.matrixSubtraction()
