class CreateNullMAtrix:
    def matrixCreatin(self):
        Matrix = []
        Rows = int(input("Enter the Number of Rows You want in the Matrix = "))
        Column = int(input("Enter the Number of Column you want in matrix = "))

        # appending the number of Rows to the matrix
        for row in range(0, Rows):
            Matrix.append([])

        # appending the zeros to the matrix
        for row in range(0, Rows):
            for col in range(0, Rows):
                Matrix[row].append(col)
                Matrix[row][col] = 0

        # printing the matrix which contains zeros
        print("Matrix is created initially contains zero value :")
        for values in Matrix:
            print(values)
        print("\n")
        return Matrix

