'''This class is used for the Automation of stack '''
import string
from random import randint
from StackExample.Stack import Stack
class AutomateStack:
    def __init__(self):
        self.random = randint(0, 1000)
        self.stack = [10, 3]

    def comparebeforeSize(self, size1, size2):
        if size1 == size2:
            print('Test For Size Of Stack is Passed\n')
        else:
            print("Test case of check size Before  Failed\n")

    def comparsizeafter(self, size0, size1):
        if size0 == size1:
            print('Test For Size Of Stack  Passed\n')
        else:
            print("Test case of check size Failed\n")


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

        # compare size
        self.comparebeforeSize(sizeBefore, sizeBeforePushOfStackUsingFunction)
        self.comparsizeafter(sizeAfter, sizeAfterPushOfStackUsingFunction)

        print('*' * 60)
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

        self.comparebeforeSize(sizeBeforePopOfStackA, sizeBeforePopUsingFun)
        self.comparsizeafter(sizeAfterPopOfStackA, sizeAfterPopUsingFun)
        print('*' * 60)

    # checking pop from the Empty stack
    def checkPopFromEmpty(self):
        print('Checking Pop from the Empty stack using Automation ')
        self.stack.clear()
        print("Stack = ", self.stack)

        try:
            self.stack.pop(0)
        except IndexError:
            print("list is empty you cannot pop value")
            print("Test case is passed\n")

        # using function
        print("**Using Function**")
        print("stack = ", self.stack)
        print("Trying to Pop from Empty list")
        d = Stack()
        d.items.clear()  # clear All list
        d.pop()
        print(" Test case is Passed using the Function is passed")
        print('*' * 60)

        # checking the push operation
    def checkPushOperation(self):
        # using the automation
        print('Test case for Push Operation')
        self.stack.append(int(self.random))
        print("Push Element is : ", self.random)
        # checking is stack contains
        if self.random in self.stack:
            print(self.random, "data is present in the list")
        print("PUSH data using Automation contains", self.stack, '\n')
        self.stack.pop(len(self.stack) - 1)

        # using the function
        print('The pop Operation Using Function')
        q = Stack()
        q.push(int(self.random))
        # checking is stack contains data or not
        if self.random in q.items:
            print("Is present in stack ", self.random)
        else:
            print("Test case Failed")
        print('*' * 60)

    # checking the pop operation
    def checkPopOperation(self):

        print("POP Data using Automation")
        print('Initially Stack contains =', self.stack)
        popitemindex = len(self.stack)-1
        popitem = self.stack[popitemindex]
        print('popitem', self.stack[popitemindex])
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
        print('*'*60)


sa = AutomateStack()
sa.checkPushOperation()
sa.checkPopOperation()
sa.checkSizeBeforeAndAfterPush()
sa.checkSizeBeforeAndAfterPop()
sa.checkPopFromEmpty()
