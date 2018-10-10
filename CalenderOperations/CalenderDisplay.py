
class Calender:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December', ]
    daysInMonths = [range(1,31 + 1),range(1,28 + 1), range(1,31 + 1), range(1,30 + 1), range(1,31 + 1), range(1,30 + 1)
        , range(1,31 + 1), range(1,31 + 1), range(1,30 + 1), range(1,31 + 1), range(1,30 + 1), range(1,31 + 1)]

    def __init__(self, year):
        self.year = year

    def checkLeap(self, year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 is True:
            return True
        else:
            return False

    def displayCalender(self, year, firstDay):

        WDays = ['Su', 'M', 'T', 'W', 'Th', 'F', 'Sa']
        startPosition = WDays.index(firstDay)

        # if True, adjust Feburary date range for leap year | 29 days
        if self.checkLeap(year):
            self.daysInMonths[1] = range(1,29+1)

        for month,days in zip(self.months,self.daysInMonths):
            # Print month title
            print('{0} {1}'.format(month, year).center(20, ' '))
            # Print Day headings
            print(''.join(['{0:<3}'.format(w) for w in WDays]))
            # Add spacing for non-zero starting position
            print('{0:<3}'.format('') * startPosition, end='')

            for dates in days:
                # Print dates
                print('{0:<3}'.format(dates), end='')
                startPosition += 1

                if startPosition == 7:
                    # If start_pos == 7 (Sunday) start new line
                    print()
                    startPosition = 0  # Reset counter
            print('\n')

year = int(input('Enter year'))
firstDay = input("The first day of the month: Like this 'Su', 'M', 'T', 'W', 'Th', 'F', 'Sa'  ").capitalize()  # The date that user wants the month to start
c = Calender(year)
c.displayCalender(year, firstDay)
