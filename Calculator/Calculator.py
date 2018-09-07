# Python program for simple calculator
class Calculator:

    def __init__(self):
        return None

    # Function to add two numbers
    def add(self, num1, num2):
        return num1 + num2

    # Function to subtract two numbers
    def subtract(self,num1, num2):
        return num1 - num2

    # Function to multiply two numbers
    def multiply(self,num1, num2):
        return num1 * num2

    # Function to divide two numbers
    def divide(self,num1, num2):
        return num1 / num2

    ''' This method is used for calling the method of the class
         Add,subtract,Multiply,divide
    '''

    def callingCalculator(self):
        while True:
            print("\n\nPlease select operation -\n" "\t1. Add\n" "\t2. Subtract\n" "\t3. Multiply\n" "\t4. Divide\n" "\t5. Quit\n")

            select = int(input("Select operations form 1, 2, 3, 4 :"))

            if select == 1:
                number1 = int(input("Enter first number: "))
                number2 = int(input("Enter second number: "))
                print(number1, "+", number2, "=",
                      self.add(number1, number2))

            elif select == 2:
                number1 = int(input("Enter first number: "))
                number2 = int(input("Enter second number: "))
                print(number1, "-", number2, "=",
                      self.subtract(number1, number2))

            elif select == 3:
                number1 = int(input("Enter first number: "))
                number2 = int(input("Enter second number: "))
                print(number1, "*", number2, "=",
                      self.multiply(number1, number2))

            elif select == 4:
                number1 = int(input("\tEnter first number: "))
                number2 = int(input("\tEnter second number: "))
                try:
                    print(number1, "/", number2, "=",
                    self.divide(number1, number2))

                except ZeroDivisionError:
                        print("\n\t\t", number1, "/", number2, "=", "Infinity")

            elif select == 5:
                print('Exited successfully')  # user will exit the process successfully
                break

            elif select != 1 or select != 2 or select != 3 or select != 4 or select != 5:
                print("Invalid Input")












