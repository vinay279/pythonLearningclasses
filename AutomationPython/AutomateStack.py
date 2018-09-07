'''This class is used for the Automation of stack '''
import string
from random import *
from StackExample.Stack import Stack
class AutomateStack:
    def __init__(self):
        self.random = "".join(choice(string.ascii_letters + string.digits) for x in range(randint(3, 16)))
        self.items = []
    # for genrate Randoms Strings

    def AutomateStackPush(self):
        # pushing data in the stack by using the Automation
        #data = self.random
        randm = "".join(choice(string.ascii_letters + string.digits) for x in range(randint(8, 16)))
        self.items.append(randm)
        print("Data is PUSH using Automation code",randm)
        print(" The List  =", self.items)

       # By using the function present in code

    def pushUsingFunction(self):
        random1 = "".join(choice(string.ascii_letters + string.digits) for x in range(randint(3, 5)))
        d = Stack()
        d.push(random1)
        d.push(random1+'PUSH')
        print("Data is PUSH using the Function",random1)
        print("The List = ",self.items)
        d.pop()
        print("The List = ", self.items)



    def AutomatePOP(self):
        self.items.pop











A = AutomateStack()
A.AutomateStackPush()
A.pushUsingFunction()
