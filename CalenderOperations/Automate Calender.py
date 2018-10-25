from random import randint
from calendar import Calendar as a
from CalenderOperations.CalenderDisplay import Calender

"""class for automating the the calender"""
class AutomateCalender:
    date = randint(1,31)
    month = randint(1,12)
    year = randint(1900,3000)
    c = Calender()

    def displayInCheckFirstDay(self):
        m = self.c.HighlightDateAndDay(self.date,self.month,self.year)
        a.monthdatescalendar(self.year, self.month)
        return m


    def checkYearIsCorrect(self):
        m = self.c.displayCalender(self.year)
        if m is True:
            print("test case is passed")
        exit()

s = AutomateCalender()
s.displayInCheckFirstDay()
s.checkYearIsCorrect()