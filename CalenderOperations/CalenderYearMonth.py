class CalenderYearMonth:
    year = int(input('Enter year'))
    month = int(input("Enter Month "))

    def printMonthAndYear(self, month, year):

        if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            return 31
        elif month == 4 or 6 or 9 or 11:
            return 30
        elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and month == 2 is True:
            return 29

        if month == 1:
            print('\t\tJanuary', ' ', year)

        elif month == 2:
            print('\t\tFebruary', ' ', year)
            return 28
        elif month == 3:
            print('\t\tMarch', ' ', year)
        elif month == 4:
            print('\t\tApril', ' ', year)
        elif month == 5:
            print('\t\tMay', ' ', year)
        elif month == 6:
            print('\t\tJune', ' ', year)
        elif month == 7:
            print('\t\tJuly', ' ', year)
        elif month == 8:
            print('\t\tAugust', ' ', year)
        elif month == 9:
            print('\t\tSeptember', ' ', year)
        elif month == 10:
            print('\t\tOctober', ' ', year)
        elif month == 11:
            print('\t\tNovember', ' ', year)
        elif month == 12:
            print('\t\tDecember', ' ', year)

    # daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def noOfDaysInMonth(self):

        if self.month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            return 31

        if self.month == 4 or 6 or 9 or 11:
            return 30
        elif self.month == 2:
            self.checkLeap()

    def checkLeap(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return 29
        else:
            return 28