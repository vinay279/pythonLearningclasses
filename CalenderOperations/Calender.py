import calendar
from datetime import date
a = date(date.today().year, 1, 1)
class Calender:
    monthCal = []
    Months = ["jan", "feb", "mar", "april", "may", "june",
              "july", "aug", "sept", "oct", "nov", "dec"]
    Day = ['S', 'M', 'Tu', 'W', 'Th', 'F', 'S']

    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def numberOfMaxDay(self):
        year = int(input("Enter the Year"))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            self.daysInMonths[1] = 29

        month = int(input('Enter the Month EX- For Jan - 1, For Dec - 12'))
        day = int(input('enter day EX- For sunday enter- 1 ,for monday enter 2, for saturday enter -7'))
        if day == 1:
            for rows in range(0, 6):
                self.monthCal.append([])

            for row in range(0, 6):
                for col in range(0, len(self.Day)):
                    self.monthCal[row].append(col)

                    if row == 0:
                        self.monthCal[0][col] = self.Day[col]
                    elif row != 0:
                        date =0
                        date +=1
                        self.monthCal[row][col] = date+1



        for val in self.monthCal:
            print(val)


    def inputCalender(self,syear):

        year = int(input("Enter the Year"))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            Calender.numberOfMaxDay(self).daysInMonths[1] = 29
        month = int(input('Enter the Month EX- For Jan - 1, For Dec - 12'))
        if month == 1:
            return ''








    def find1stDayOfYear(self,dayOfWeekInNo):
        dayOfWeekInNo = 0

        if dayOfWeekInNo == 1:
            self.ssss


    def findADay(self,date,month,year):
        date = 0
        month = 0
        year = 0
        N = date + (2 * month) + (3 * (month + 1) // 5) + (year + (year / 4) - (year / 100) )+ (year / 400) + 2
        Day = N % 7
        print(Day)



c = Calender()
c.numberOfMaxDay()




