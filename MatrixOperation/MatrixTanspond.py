''' class doing transpose Matrix Operation '''

class TransposeMatrix:

    def transposeMatrix(self):
        rowINM = int(input("Enter the Numbers of Rows "))
        colsInM = int(input("Enter the Numbers of Column"))

        Matrix=[]

        for rowsinmat in range(0, rowINM):
            Matrix.append([])

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


        result= []
        for colinresult in range(0,colsInM):
            result.append([])
        for col in range(0, rowINM):
            for row in range(0, colsInM):
                result[row].append(col)
                result[row][col] = 0


        for row in range(len(Matrix)):
            # iterate through columns
            for col in range(len(Matrix[0])):
                result[col][row] = Matrix[row][col]
        print("The Transposed of given Matrix is :")
        for r in result:
            print(r)
        print(len(Matrix))
        print(len(result))

t= TransposeMatrix()
t.transposeMatrix()