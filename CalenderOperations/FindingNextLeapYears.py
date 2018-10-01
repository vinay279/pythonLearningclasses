import datetime as d
class FindLeapYears:

    def findYear (self, year):
        count = 0
        leapYears = []
        while count <= 20:
            year += 1
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                count += 1
                leapYears.append(year)
        print('This are 20 leap years after the year =', leapYears)

    def findNxtLeapYearsByUsingSystemYear(self):
        year = int(d.datetime.now().year)
        print('This is current year = ', year)
        self.findYear(year)

    def findLeapYearsByUserInputedYear(self):
        year = int(input("Enter The Year You Want"))
        self.findYear(year)



