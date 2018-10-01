from CalenderOperations.FindingNextLeapYears import FindLeapYears as y

class Calender:
    monthCal = []
    Months = ["jan", "feb", "mar", "april", "may", "june",
              "july", "aug", "sept", "oct", "nov", "dec"]
    Day = ['S', 'M', 'Tu', 'W', 'Th', 'F', 'S']

    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def numberOfMaxDay(self):

        for rows in range(0, 6):
            self.monthCal.append([])

        for row in range(0, 6):
            for col in range(0, len(self.Day)):
                self.monthCal[row].append(col)

                if row == 0:
                    self.monthCal[0][col] = self.Day[col]
        for val in self.monthCal:
            print(val)


    def inputCalender(self, first, day):

        year = int(input("Enter the Year"))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            Calender.numberOfMaxDay(self).daysInMonths[1] = 29
        month = int(input('Enter the Month EX- For Jan - 1, For Dec - 12'))
        if month == 1:
             






    def find1stDayOfYear(self,date, year):
        date = int(input('Enter the date'))
        month = int(input('Enter month : For Ex - '))
        year = int(input('Enter year'))


    def findADay(self,date,month,year):
        date = int(input('Enter the date'))
        month = int(input('Enter month : For Ex - '))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            self.daysInMonths[1] = 29




c = Calender()
c.numberOfMaxDay()




