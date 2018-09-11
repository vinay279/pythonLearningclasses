import random


class MatrixAddition:

    m1 = input("Enter No. of rows in the first matrix: ")
    n1 = input("Enter No. of columns in the first matrix: ")
    a = [[ for col in range(n1)] for row in range(m1)]
    print("Enter Elements: ")
    for i in range(m1):
        for j in range(n1):
            a[i][j] = input()
    m2 = input("Enter No. of rows in the second matrix: ")
    n2 = input("Enter No. of columns in the second matrix: ")
    b = [[random.random() for col in range(n2)] for row in range(m2)]
    print("Enter Elements: ")
    for i in range(m2):
        for j in range(n2):
            b[i][j] = input()
    c = [[random.random() for col in range(n1)] for row in range(m1)]
    if ((m1 == m2) and (n1 == n2)):
        print("output is")
        for i in range(m1):
            for j in range(n1):
                c[i][j] = a[i][j] + b[i][j]
                print(c[i][j], '\t',)
            print()
    else:
        print("Matrix addition not possible")

    '''print("enter n for nxn matrix")
    n = input()

    matrix1 = []
    matrix2 = []

    # taking elements of first matrix

    print("Enter elements of first matrix")
    for i in range(0, n):
        # taking elements of first column

        print("Enter elements of ", i, "column, seperated by space")

        # raw_input().split() will split the string
        # '1 2 34'.split() will give ['1', '2', '34']
        # map will convert its elements into integers [1, 2, 34]

        matrix1.append(map(int, input().split()))

    print("Matrix 1 is", matrix1)

    # taking elements of second matrix

    print("Enter elements of second matrix")
    for i in range(0, n):
        # Similar to input taken for 1 matrix

        print("Enter elements of ", i, "column, seperated by space")
        matrix2.append(map(int, input().split()))

    print("Matrix 2 is", matrix2)

    # adding

    add_matrix = []
    for i in range(0, n):
        a = []
        for j in range(0, n):
            # making a addition matrix's column to append
            # making a 1D matrix with elements as sum of elements of
            # respective columns of both matrices

            a.append(matrix1[i][j] + matrix2[i][j])
        add_matrix.append(a)
    print("Addition of matrix is", add_matrix)

    # multiplication
    multi_matrix = []
    for i in range(0, n):
        a = []
        for j in range(0, n):
            summ = 0
            for k in range(0, n):
                summ = summ + (matrix1[i][k] * matrix2[k][j])
            a.append(summ)
        multi_matrix.append(a)
    print("matrix1 x matrix 2 =", multi_matrix)

    # transpose of matrix1

    tr_matrix = []

    for i in range(0, n):
        a = []
        for j in range(0, n):
            # matrix1[j][i] will give row of matrix 1
            # we are making it column of new matrix
            a.append(matrix1[j][i])
        tr_matrix.append(a)

    print("Transpose of matrix 1 is", tr_matrix)'''


