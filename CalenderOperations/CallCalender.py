from CalenderOperations.CalenderDisplay import Calender
class CallCalender:
    def callCal(self):
        while True:
            print('\t\t****CALENDER****\n'
                  '1.Display Month Calender\n'
                  '2.Display Year Calender\n'
                  '3.Highlight Date in Calender\n'
                  '4.Exit')
            UserInput = int(input("Select Operation you want"))
            C = Calender()
            if UserInput == 1:
                month = int(input('Enter Month'))
                Year = int(input('Enter Year'))
                C.printMonthCalender(month,Year)
            elif UserInput == 2:
                Year = int(input('Enter Year'))
                C.displayCalender(Year)
            elif UserInput == 3:
                date = int(input("Enter Date"))
                month = int(input('Enter Month'))
                year = int(input('Enter Year'))
                C.HighlightDateAndDay(date, month, year)
            elif UserInput == 4:
                break



c = CallCalender()
c.callCal()