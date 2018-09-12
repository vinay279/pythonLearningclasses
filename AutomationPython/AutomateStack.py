'''This class is used for the Automation of stack '''
import string
from random import randint
from StackExample.Stack import Stack
class AutomateStack:
    def __init__(self):
        self.random = randint(0, 1000)
        self.stack = [10, 3]

    def checkSizeBeforeAndAfterPush(self):
        # using Automation
        print("Checking the size of stack after push  \n")
        print('Initially Stack contains =', self.stack)
        sizeBefore = len(self.stack)
        print('Size of stack before push is = ', sizeBefore)
        self.stack.append(self.random)
        sizeAfter = len(self.stack)
        print('Size of stack after push is = ', sizeAfter)
        print('Stack contains after push', self.stack, '\n')

    # using function
        print("Checking Size Of Stack Before and after push using function")
        q = Stack()
        print('Initially Stack contains =', q.items)
        sizeBeforePushOfStackUsingFunction = len(q.items)

        q.push(self.random)
        sizeAfterPushOfStackUsingFunction = len(q.items)

        if sizeBefore == sizeBeforePushOfStackUsingFunction :
            print('Test For Size Of Stack Before PUSH Data Passed\n')
        else:
            print("Test case of check size Before PUSH Data Failed\n")

        if sizeAfter == sizeAfterPushOfStackUsingFunction:
            print('Test For Size Of Stack After PUSH Data Passed\n')
        else:
            print("Test case of check size After PUSH Data Failed\n")


                         #method for checking the size of stack

    def checkSizeBeforeAndAfterPop(self):
        # using automated task
        print("Checking The Size before And after POP Data using Automation")
        print('Initially Stack contains =', self.stack)
        sizeBeforePopOfStackA = len(self.stack)
        print('Size of stack before pop', len(self.stack))
        self.stack.pop(len(self.stack) - 1)
        sizeAfterPopOfStackA = len(self.stack)
        print('Size of stack after pop', len(self.stack))
        print('Stack contains after pop', self.stack, '\n')

        # using the function
        s = Stack()
        print("Checking The Size before And after POP Data using function")
        print('Initially Stack contains in function =', s.items)
        sizeBeforePopUsingFun = len(s.items)
        print('Size of stack before pop', len(s.items))
        s.pop()
        sizeAfterPopUsingFun = len(s.items)
        print('Size of stack After pop using function', len(s.items))

        if sizeBeforePopOfStackA == sizeBeforePopUsingFun:
            print('Test For Size Of Stack Before POP Data Passed\n')
        else:
            print("Test case of check size Before POP Data Failed\n")

        if sizeAfterPopOfStackA == sizeAfterPopUsingFun:
            print('Test For Size Of Stack After POP Data Passed\n')
        else:
            print("Test case of check size After POP Data is Failed\n")


    # checking pop from the Empty stack
    def checkPopFromEmpty(self):
        print(' Checking Pop from the Empty stack using Automation ')
        self.stack.clear()
        print(self.stack)

        try:
            self.stack.pop(0)
        except IndexError:
            print("list is empty you cannot pop value")
            print("Test case is passed\n")

        # using function
        print("Trying to Pop from Empty list")
        d = Stack()
        d.items.clear()  # clear All list
        d.pop()
        print(" Test case is Passed using the Function is passed")

        # checking the push operation
    def checkPushOperation(self):
        # using the automation
        self.stack.append(int(self.random))
        # checking is stack contains
        if self.random in self.stack:
            print(self.random, "data is present in the list")
        print(" PUSH data using Automation contains", self.stack, '\n')
        self.stack.pop(len(self.stack) - 1)

        # using the function
        print('The pop Operation Using Function')
        q = Stack()
        q.push(int(self.random))
        # checking is stack contains data or not
        if self.random in q.items:
            print(self.random, "Is present in stack ")
        else:
            print("Test case Failed")

    # checking the pop operation
    def popOperation(self):

        print("POP Data using Automation")
        print('Initially Stack contains =', self.stack)
        popitemindex = len(self.stack)-1
        popitem = self.stack[popitemindex]
        print(' popitem', self.stack[popitemindex])
        self.stack.pop(len(self.stack) - 1)
        if popitem not in self.stack:
            print(popitem, "Is Not present in stack ")
            print('Stack contains after pop', self.stack, '\n')

        # using the function
        s = Stack()
        print("POP Data using function")
        print('Initially Stack contains =', s.items)
        popitemindex = len(s.items) - 1
        popitem = s.items[popitemindex]
        print(' popitem', s.items[popitemindex])
        s.pop()
        if popitem not in s.items:
            print(popitem, "Is Not present in stack ")
            print('Stack contains after pop', s.items, '\n')
            print("Test case is pass")
        else:
            print("Test case Failed")


sa = AutomateStack()
sa.popOperation()
