import calendar
class cal:

    def takeInput(self):
        year = int(input('Enter year'))
        month = int(input('Enter Month'))

        if month in range(1,13) :
            print("Wrong input!")
        else:
            self.printMonth(year, month)

    def printMonth(self,year, month):
        self.printMonthTitle(year, month)
        self.printMonthBody(year, month)

    def printMonthTitle(self,year, month):
        print("         " , self.getMonthName(month) , " " ,year)
        print("–––––––––––––––––––––––––––––")
        print(" Sun Mon Tue Wed Thu Fri Sat")

    def getMonthName(self, month):

        if month == 1: return 'January'
        elif month == 2:return 'February'
        elif month == 3:return 'March'
        elif month == 4:return 'April'
        elif month == 5:return 'May'
        elif month == 6:return 'June'
        elif month == 7:return 'July'
        elif month == 8:return 'August'
        elif month == 9:return 'September'
        elif month == 10:return 'October'
        elif month == 11:return 'November'
        elif month == 12:return 'December'

    def printMonthBody(self, year, month):
        startDay = self.getStartDay(year, month)
        numberOfDaysInMonth = self.getNumberOfDaysInMonth(year, month)

        # Pad space before the first day of the month
        pad = 0
        while pad < startDay:
            print("    ")
        i = 1
        while i < numberOfDaysInMonth:
            if i < 10:
                print("   ",  i)
            elif (i + startDay) % 7 == 0:
                 print('  ')
            else:
                print("  " , i)


    def getTotalNumberOfDays(self,year,month):
        for year in range(1800,3001):
            if self.isLeapYear(year) is True:
                return 366
            else:
                return 365



        for month in range(1, 13):
            total = total + self.getNumberOfDaysInMonth(year, month)

        return total

    def getStartDay(self, year,  month):
        startDay1800 = 3
        totalNumberOfDays = self.getTotalNumberOfDays(year, month)
        return (totalNumberOfDays + startDay1800) % 7

    def getNumberOfDaysInMonth(self,year, month):

        if (month == 1 and month == 3 and month == 5 and month == 7 and
            month == 8 and month == 10 and month == 12):
            return 31

        if month == 4 and month == 6 and month == 9 and month == 11:
            return 30

        if month == 2:
            if self.isLeapYear(year) is True:
                return 29
            else: return 28


    def isLeapYear(self, year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False





x= cal()
x.takeInput()


















