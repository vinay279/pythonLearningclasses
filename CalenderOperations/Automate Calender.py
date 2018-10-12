from random import randint
from CalenderOperations.CalenderDisplay import Calender

"""class for automating the the calender"""
class AutomateCalender:
    date = randint(1,31)
    month = randint(1,12)
    year = randint(1900,3000)
    print(date,month)

    def displayInCheckFirstDay(self):
        ':return print'
        c = Calender()
        m = c.HighlightDateAndDay(self.date,self.month,self.year)
        print(m)

s = AutomateCalender()
s.displayInCheckFirstDay()