import calendar

class Calender:

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December', ]
    daysInMonths = [range(1, 31 + 1),range(1, 28 + 1), range(1,31 + 1), range(1,30 + 1), range(1,31 + 1), range(1,30 + 1)
        , range(1,31 + 1), range(1,31 + 1), range(1,30 + 1), range(1,31 + 1), range(1,30 + 1), range(1,31 + 1)]

    WDays = ['M', 'T', 'W', 'Th', 'F', 'Sa', 'Su']

    #check year leap or not
    def checkLeap(self, year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 is True:
            self.daysInMonths[1] = range(1, 29 + 1)
        else:
            self.daysInMonths[1] = range(1, 28 + 1)

    # method for displaying calender
    def displayCalender(self, year):
        month, day = 1, 1
        firstDay = calendar.weekday(year, month, day)
        startPosition = firstDay
        self.checkLeap(year)

        for month, days in zip(self.months, self.daysInMonths):
            # Print month title
            print('{0} {1}'.format(month, year).center(20, ' '))
            # Print Day headings
            print(''.join(['{0:<3}'.format(w) for w in self.WDays]))
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

    def printMonthCalender(self,month,year):
        det = 1
        FirstDay = calendar.weekday(year, month, det)
        Month = self.months[month-1]
        Dates = self.daysInMonths[month-1]
        self.checkLeap(year)
        print('{0} {1}'.format(Month, year).center(20, ' '))
        print('\033[94m'+''.join(['{0:<3}'.format(w) for w in self.WDays])+'\033[0m')
        print('{0:<3}'.format('') * FirstDay, end='')
        for date in Dates:
            print('{0:<3}'.format(date), end='')
            FirstDay += 1
            if FirstDay == 7:
                print()
                FirstDay = 0  # Reset counter
        print("\n")

    # method for highlighting the date in the in the calender
    def HighlightDateAndDay(self,WantedDate, month, year):
        det = 1
        FirstDay = calendar.weekday(year, month, det)
        Month = self.months[month - 1]
        Dates = self.daysInMonths[month - 1]
        self.checkLeap(year)
        print('{0} {1}'.format(Month, year).center(20, ' '))
        print('\033[94m' + ''.join(['{0:<3}'.format(w) for w in self.WDays]) + '\033[0m')
        print('{0:<3}'.format('') * FirstDay, end='')
        d = ''
        for date in Dates:
            if date == WantedDate:
                print('\033[1m'+'\033[93m'+'{0:<3}'.format(date), end='' + '\033[0m')
                d = self.WDays[FirstDay]
                FirstDay += 1
                if FirstDay == 7:
                    print()
                    FirstDay = 0  # Reset counter

            else:
             print('{0:<3}'.format(date), end='')
             FirstDay += 1
             if FirstDay == 7:
                 print()
                 FirstDay = 0  # Reset counter

        print("\n")
        s = self.months[month-1] + ' ' + str(year), 'day  === ' + d
        return print(s)









