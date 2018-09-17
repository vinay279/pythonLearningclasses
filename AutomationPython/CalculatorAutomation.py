''' This class is used for the calculator automation '''

# importing th calculator class
from Calculator.Calculator import Calculator
import random

class AutomateCalculator:
    # defination for the calculator Automation

    def __init__(self):
        self.randomNO2 = random.randint(0, 1000)
        self.randomNO1 = random.randint(0, 1000)

    def automateAdd(self):
        print(" Test Case for  Addition ")
        print(self.randomNO2, "- This is first Random number ")
        print(self.randomNO1, "- This is second Random number ")
        num1 = self.randomNO1
        num2 = self.randomNO2
        print("Addition by Automated funnction =", num1 + num2)


        # By using the function
        c = Calculator()
        sum2 = c.add(num1, num2)
        print("Addition Output by Calling function =", sum2)

        if num1 + num2 == sum2:
            print("Test case of calculator is passed\n\n")

        else:
            print(" Test Automation of of Calculator Addition is failed ")
        print('*' * 70)

    def automateSubtraction(self):
        print("Test Case for Subtraction")
        print(self.randomNO2, "- This is first Random number ")
        print(self.randomNO1, "- This is second Random number ")
        num1 = self.randomNO1
        num2 = self.randomNO2
        print("Subtraction by Automated function =", num1 - num2)

        # By using the function
        c = Calculator()
        subtraction = c.subtract(num1, num2)
        print("Subtraction Output by Calling function =", subtraction)

        if num1 - num2 == subtraction:
            print("Test case of calculator Subtraction passed\n\n")

        else:
            print(" Test Automation of of Calculator Subtraction is failed ")
        print('*' * 70)

    # Automation test for the Multiply
    def automateMultiply(self):
        print(" Test Case for Multiplication ")
        print(self.randomNO2, "- This is first Random number ")
        print(self.randomNO1, "- This is second Random number ")
        num1 = self.randomNO1
        num2 = self.randomNO2
        print("Multiply by Automated function =", num1 * num2)

        # By using the function
        c = Calculator()
        Multiply = c.multiply(num1, num2)
        print("Multiply Output by Calling function =", Multiply)

        if num1 * num2 == Multiply:
            print("Test case of calculator Multiply is passed\n\n")

        else:
            print(" Test Automation of of Calculator Multiply is failed ")
        print('*' * 70)

    # Automated test for the division
    def automateDivision(self):
        print(" Test Case for Division ")
        print(self.randomNO2, "- This is first Random number ")
        print(self.randomNO1, "- This is second Random number ")
        num1 = self.randomNO1
        num2 = self.randomNO2
        try:
            print("Division by Automated function =", num1 / num2)

        except ZeroDivisionError:
            print(num1, "/", num2, " = Infinity")


        # By using the function
        c = Calculator()
        division = c.multiply(num1, num2)
        print("Division Output by Calling function =", division)

        if num1 * num2 == division:
            print("Test case of calculator Division is passed\n\n")

        else:
            print(" Test Automation of of Calculator Division is failed ")
        print('*' * 70)







vi = AutomateCalculator()
vi.automateAdd()
vi.automateSubtraction()
vi.automateMultiply()
vi.automateDivision()


