class Calender:
    year = int(input('Enter year'))
    month = int(input("Enter Month "))

    def printMonthAndYear(self,month,year):
        if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            return 31
        if month == 4 or 6 or 9 or 11:
            return 30
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and month == 2 is True:
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


    #daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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

    def displayCalender(self):

        days = self.noOfDaysInMonth()
        print(days)
        firstDayMonth = input("The first day of the month: Like this 'Sa', 'M', 'T', 'W', 'Th', 'F', 'Su'  ")  # The date that user wants the month to start
        firstDayMonth = firstDayMonth.capitalize()

        Days = ['Sa', 'M', 'T', 'W', 'Th', 'F', 'Su']
        print('{:3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format('Sa', 'M', 'T', 'W', 'Th', 'F', 'Su'))
        #loop to generate the dates for a month
        for day in range(1, days+1):

            # for calendar formatting
          if firstDayMonth == Days[0] and day == 1:
            print('{:>3}'.format(day), end=' ')

          elif firstDayMonth == Days[1] and day == 1:
            print(' '*4+'{:>3}'.format(day), end=' ')

          elif firstDayMonth == Days[2] and day == 1:
            print(' '*8+'{:>3}'.format(day), end=' ')

          elif firstDayMonth == Days[3] and day == 1:
            print(' '*12+'{:>3}'.format(day), end=' ')

          elif firstDayMonth == Days[4] and day == 1:
            print(' '*16+'{:>3}'.format(day), end=' ')

          elif firstDayMonth == Days[5] and day == 1:
            print(' '*20+'{:>3}'.format(day), end=' ')

          elif firstDayMonth == Days[6] and day == 1:
            print(' '*24+'{:>3}'.format(day), end=' ')

          else:
            print('{:>3}'.format(day), end=' ')  # to print the remaining dates

          if firstDayMonth == Days[0] and day % 7 == 0:
            print()
          elif firstDayMonth == Days[1] and day % 7 == 6:
            print()
          elif firstDayMonth == Days[2] and day % 7 == 5:
            print()
          elif firstDayMonth == Days[3] and day % 7 == 4:
            print()
          elif firstDayMonth == Days[4] and day % 7 == 3:
            print()
          elif firstDayMonth == Days[5] and day % 7 == 2:
            print()
          elif firstDayMonth == Days[6] and day % 7 == 1:
            print()


c = Calender()
c.displayCalender()