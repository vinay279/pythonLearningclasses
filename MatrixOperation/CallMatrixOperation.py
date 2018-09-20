from MatrixOperation.AllMatrixOperations import MatrixOperations as mo
class CallMatrix:

    while True:
        print('\n')
        print("***Select the sorting option You want to sort***")
        print("\t1.Matrix Addition\n"
              "\t2.Matrix Subtraction\n"
              "\t3.Matrix Multiplication\n"
              "\t4.Identity Matrix \n"
              "\t5.Diagonal Matrix\n"
              "\t6.Lower Triangular Matrix\n"
              "\t7.Upper Triangular Matrix\n"
              "\t8.Exit \n")
        m = mo()
        menu = int(input('input = '))
        if menu == 1:
            m.matrixAddition()

        elif menu == 2:
            m.matrixSubtraction()

        elif menu == 3:
            m.MatrixMultiplication()

        elif menu == 4:
            m.createIdentityMatrix()

        elif menu == 5:
            m.createDiagonalMatrix()

        elif menu == 6:
            m.lowerTriangularMat()

        elif menu == 7:
            m.upperTriangularMat()

        elif menu == 8:
            break

        else:
            print("Invalid Operation ")
