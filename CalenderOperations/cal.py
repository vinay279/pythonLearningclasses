import calendar
class cal:
    calendar.month(year, month)
    def takeInput(self):
        year = int(input('Enter year'))
        month = int(input('Enter Month'))

        if month < 1 and month > 12 and year < 1980:
            print("Wrong input!")
        else:
            self.printMonth(year, month)

    def printMonth(self,year, month):
        self.printMonthTitle(year, month)
        self.printMonthBody(year, month)

    def printMonthTitle(self,year, month):
       print("         " + self.getMonthName(month) + " " + year)
       print("–––––––––––––––––––––––––––––")
       print(" Sun Mon Tue Wed Thu Fri Sat")

    def getMonthName(self, month):

        if   month == 1:return 'January'
        elif month == 2:return 'February'
        elif month == 3:return 'March'
        elif month == 4:return 'April'
        elif month == 5:return 'May'
        elif month == 6:return 'June'
        elif month == 7:return 'July'
        elif month == 8:return 'August'
        elif month == 9:return 'September'
        elif month == 10:return 'October'
        elif month == 11:return 'November'
        elif month == 12:return 'December'

    def printMonthBody(self, year, month):
        startDay = self.getStartDay(year, month)
        numberOfDaysInMonth = self.getNumberOfDaysInMonth(year, month)

        pad = 0
        while pad < startDay:
            print("    ")
            i = 1
            while i < numberOfDaysInMonth:
                if i <10:
                    print("   ", + i)
                else:
                    print("  " ,+ i)
        if ((i + startDay) % 7 == 0:


        System.out.println()



























    /** Print the calendar for a month in a year */

     static void printMonth(int year, int month) {

     //Print the headings of the calendar
      printMonthTitle(year, month);

     //Print the body of the calendar
      printMonthBody(year, month);
    }

    /** Print the month title, e.g., May, 1999 */

    static void printMonthTitle(int year, int month) {

    System.out.println("         " + getMonthName(month) + " " + year);
    System.out.println("–––––––––––––––––––––––––––––");
    System.out.println(" Sun Mon Tue Wed Thu Fri Sat");

    }

    /** Get the English name for the month */
    static String getMonthName(int month) {
      String monthName = null;
      switch (month) {
        case 1: monthName = "January"; break;
        case 2: monthName = "February"; break;
        case 3: monthName = "March"; break;
        case 4: monthName = "April"; break;
        case 5: monthName = "May"; break;
        case 6: monthName = "June"; break;
        case 7: monthName = "July"; break;
        case 8: monthName = "August"; break;
        case 9: monthName = "September"; break;
        case 10: monthName = "October"; break;
        case 11: monthName = "November"; break;
        case 12: monthName = "December";
      }
      return monthName;
    }

    /** Print month body */
    static void printMonthBody(int year, int month) {

      // Get start day of the week for the first date in the month
      int startDay = getStartDay(year, month);

      // Get number of days in the month
      int numberOfDaysInMonth = getNumberOfDaysInMonth(year, month);

      // Pad space before the first day of the month
      int i = 0;
      for (i = 0; i < startDay; i++)
        System.out.print("    ");
      for (i = 1; i <= numberOfDaysInMonth; i++) {
        if (i < 10)
          System.out.print("   " + i);
        else
          System.out.print("  " + i);
        if ((i + startDay) % 7 == 0)
          System.out.println();
      }
      System.out.println();
    }

    /** Get the start day of the first day in a month */

   static int getStartDay(int year, int month) {

      //Get total number of days since 1/1/1800
      int startDay1800 = 3;
      int totalNumberOfDays = getTotalNumberOfDays(year, month);

      //Return the start day
      return (totalNumberOfDays + startDay1800) % 7;
    }

    /** Get the total number of days since January 1, 1800 */

    static int getTotalNumberOfDays(int year, int month) {
     int total = 0;

     //Get the total days from 1800 to year - 1
     for (int i = 1800; i < year; i++)
     if (isLeapYear(i))
        total = total + 366;
      else
        total = total + 365;

      //Add days from January to the month prior to the calendar month
      for (int i = 1; i < month; i++)
        total = total + getNumberOfDaysInMonth(year, i);

      return total;
    }

    /** Get the number of days in a month */

    static int getNumberOfDaysInMonth(int year, int month) {
      if (month == 1 || month == 3 || month == 5 || month == 7 ||
        month == 8 || month == 10 || month == 12)
        return 31;

      if (month == 4 || month == 6 || month == 9 || month == 11)
        return 30;

      if (month == 2) return isLeapYear(year) ? 29 : 28;

      return 0; // If month is incorrect
    }

    /** Determine if it is a leap year */
    static boolean isLeapYear(int year) {
      return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
    }
}