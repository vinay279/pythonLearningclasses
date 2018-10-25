class j:
    Matrix = []

    def printboard(self):
        print('\t 0\t\t1\t\t2')
        print('\t 3\t\t4\t\t5')
        print('\t 6\t\t7\t\t8')

    def CreateDisplay(self):
        for row in range(0, 3):
            self.Matrix.append([])

            # appending the zeros to the matrix
        for row in range(0, 3):
            for col in range(0, 3):
                self.Matrix[row].append(col)
                self.Matrix[row][col] = '*'


        while True:
            val = int(input('value'))
            if val == 0:
                self.Matrix[0][0]= 'x'
                break
            if val == 1:
                self.Matrix[0][1] = 'x'
            if val == 2:
                self.Matrix[0][2] = 'x'
            if val == 3:
                self.Matrix[1][0] = 'x'
            if val == 4:
                self.Matrix[1][1] = 'x'
            if val== 5:
                self.Matrix[1][2] = 'x'
            if val== 6:
                self.Matrix[2][0] = 'x'
            if val== 7:
                self.Matrix[2][1] = 'x'
            elif val== 1:
                self.Matrix[2][2] = 'x'
            for val in self.Matrix:
                 print(val)

m = j()
m.printboard()

m.CreateDisplay()

