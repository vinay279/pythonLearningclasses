
class Calender:
    def __init__(self, year):

        self.year = year

    def checkLeap(self):
        retur = 0
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0 is True:
                retur = 29
        else:
            retur = 28
        return retur

    def displayMonthYearInfo(self, month, year):
        retur = 0

        if month == 1:
            print('\t\tJanuary', ' ', year)
            retur = 31
        elif month == 2:
            print('\t\tFebruary', ' ', year)
            retur = self.checkLeap()

        elif month == 3:
            print('\t\tMarch', ' ', year)
            return 31
        elif month == 4:
            print('\t\tApril', ' ', year)
            retur = 30
        elif month == 5:
            print('\t\tMay', ' ', year)
            return 31
        elif month == 6:
            print('\t\tJune', ' ', year)
            retur = 30
        elif month == 7:
            print('\t\tJuly', ' ', year)
            retur = 31
        elif month == 8:
            print('\t\tAugust', ' ', year)
            retur = 31
        elif month == 9:
            print('\t\tSeptember', ' ', year)
            retur = 30
        elif month == 10:
            print('\t\tOctober', ' ', year)
            retur = 31
        elif month == 11:
            print('\t\tNovember', ' ', year)
            retur = 30
        elif month == 12:
            print('\t\tDecember', ' ', year)
            retur = 31
        return retur

    def displayCalender(self, year):
        for month in range(1,13):

            days = self.displayMonthYearInfo(month, year)
            firstDayMonth = input("The first day of the month: Like this 'Su', 'M', 'T', 'W', 'Th', 'F', 'Sa'  ")  # The date that user wants the month to start
            firstDayMonth = firstDayMonth.capitalize()

            Days = ['Su', 'M', 'T', 'W', 'Th', 'F', 'Sa']
            print('{:3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format('Su', 'M', 'T', 'W', 'Th', 'F', 'Sa'))
            #loop to generate the dates for a month
            firstDay = 1
            # for calendar formatting
            if firstDayMonth == Days[0] :
                print('{:>3}'.format(firstDay), end=' ')

            elif firstDayMonth == Days[1] :
                print(' ' * 4 + '{:>3}'.format(firstDay), end=' ')

            elif firstDayMonth == Days[2]:
                print(' ' * 8 + '{:>3}'.format(firstDay), end=' ')

            elif firstDayMonth == Days[3] :
                print(' ' * 12 + '{:>3}'.format(firstDay), end=' ')

            elif firstDayMonth == Days[4] :
                print(' ' * 16 + '{:>3}'.format(firstDay), end=' ')

            elif firstDayMonth == Days[5] :
                print(' ' * 20 + '{:>3}'.format(firstDay), end=' ')

            elif firstDayMonth == Days[6] :
                print(' ' * 24 + '{:>3}'.format(firstDay), end=' ')

            for day in range(2, days+1):
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


year = int(input('Enter year'))

c = Calender(year)
c.displayCalender(year)
