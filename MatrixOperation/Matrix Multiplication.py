
class Multiplication:
    def matMul(self):

        rowINM1 = int(input('Enter the number of rows of 1st matrix :'))
        colInM1 = int(input('Enter the number of column of 1st matrix :'))
        mat1 = []
        for rowsinm1 in range(0,rowINM1):
            mat1.append([])
        print('Enter the elements of first Matrix')
        for row in range(0,rowINM1):
            for col in range(0,colInM1):
                mat1[row].append(col)
                mat1[row][col] = 0
                mat1[row][col] = int(input('-row {0} col {1} ='.format(row, col, '\n')))
        for values in mat1:
            print(values)

        rowINM2 = int(input('Enter the number of rows of 2nd matrix :'))
        colInM2 = int(input('Enter the number of rows of 2nd matrix :'))
        mat2 = []
        for rowsinm2 in range(0, rowINM2):
            mat2.append([])
        print('Enter the elements of second Matrix')
        for row in range(0, rowINM2):
            for col in range(0, colInM2):
                mat2[row].append(col)
                mat2[row][col] = 0
                mat2[row][col] = int(input('-row {0} col {1} ='.format(row, col, '\n')))
        for values in mat2:
            print(values)

        result = []

        for resultrows in range(0, rowINM2):
            result.append([])

        for row in range(0, colInM1):
            for col in range(0, rowINM2):
                result[row].append(col)
                result[row][col] = 0

        # multiplication
        if colInM1 == rowINM2:
            for rowinmat1 in range(0,len(mat1)):
                for roweleM2of0 in range(0,len(mat2[0])):
                    for rowsinm2 in range(0,len(mat2)):
                        result[rowinmat1][roweleM2of0] += mat1[rowinmat1][rowsinm2] * mat2[rowsinm2][roweleM2of0]
        else:
            print("please provide proper input")

        print("Matrix Output")
        for values in result:
            print(values)
        print("Matrix Multiplication is Performed ")







c = Multiplication()
c.matMul()
