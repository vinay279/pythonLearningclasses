'''class for printing the calender'''

class Calender:
    monthCal =[]
    daysInmonts = []
    for x in range(1, 32):
        daysInmonts.append(x)


    Day = ['S', 'M', 'Tu', 'W', 'Th', 'F', 'S']
    def PrintCalender(self):
        year = int(input('Enter year'))
        month = int(input("Enter Month "))

        if month==1:print('January', ' ', year)
        elif month == 2:print('February', ' ', year)
        elif month == 3:print('March', ' ', year)
        elif month == 4:print('April', ' ', year)
        elif month == 5:print('May', ' ', year)
        elif month == 6:print('June', ' ', year)
        elif month == 7:print('July', ' ', year)
        elif month == 8:print('August', ' ', year)
        elif month == 9:print('September', ' ', year)
        elif month == 10:print('October', ' ', year)
        elif month == 11:print('November', ' ', year)
        elif month == 12:print('December', ' ', year)

        for rows in range(0, 7):
            self.monthCal.append([])

        for row in range(0, 7):
            for col in range(0, 7):
                self.monthCal[row].append(col)
                self.monthCal[row][col] = 0

        for row in range(0, 7):
            for col in range(0, 7):
                if self.monthCal[0][col]:
                    self.monthCal[0][col] = self.Day[col]
                for val in self.daysInmonts:
                    print(val)
                    self.monthCal[row][col] = val
                    if row == 7 and col == 7:
                        break


        for val in self.monthCal:
            print(val)















c = Calender()
c.PrintCalender()