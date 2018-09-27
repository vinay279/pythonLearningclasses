import datetime as d
class FindLeapYears:

    def findNxtLeapYears(self):

        year = int(d.datetime.now().year)
        print('This is current year = ', year)
        count = 0
        leapYears = []
        while count <= 20:
            year += 1
            if (year % 4 and year % 100 and year % 400) == 0:
                count += 1
                leapYears.append(year)
        print('This are leap years after current year', leapYears)

    def findNxtLeapYearOnUserInput(self):
        year = int(input("Enter the year = "))
        count = 0
        leapYears = []
        while count <= 20:
            year += 1
            if (year % 4 and year % 100 and year % 400) == 0:
                count += 1
                leapYears.append(year)
        print('This are 20 leap years after the year =', leapYears)


c = FindLeapYears()
c.findNxtLeapYears()
