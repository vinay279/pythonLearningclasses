''' This class is calling all the operations
                  "1.Calculator"
                  "2.Stack"
                  "3.Single LinkList"
                  "4.Double Link List"
                  "5.Queue"
                  "6.Sorting"
                  "7.File IO"
                  "8.Matrix Operation"

'''

# importing classes from the
from Calculator.Calculator import Calculator
from LinklistExamples.Linklist_1 import Node,LinkedList
from LinklistExamples.DoubleLinklist import Node,DoublyLinkedList
from StackExample.Stack import Stack
from FileIO.FileIO import FileIO

from Queue.Queue import Queue
from Queue.CircularQueue import CQueue
from SortingTypes.Sorting import Sorting

class Pythonmain:
    # defination for calling calculator
    def calExecution(self):
        c = Calculator()
        c.callingCalculator()

    # calling stack for Execution
    def stackExecution(self):
        se=Stack()
        se.callingStack()

    # calling single link list for Execution
    def singleLLExecution(self):
        ll=LinkedList()
        ll.operationsLL()

    # calling Double link list for Execution
    def dLLExecution(self):
        dl = DoublyLinkedList()
        dl.operationDl()

    # calling  Queue for Execution
    def QueExecution(self):
        q=Queue()
        q.callingQueue()

    # calling circular Queue for Execution
    def CirQueueExecution(self):
        cq= CQueue()
        cq.callingCQueue()

    # calling the Sorting All methods
    def SortsExecution(self):

        s = Sorting()
        s.callSorting()

    # calling file IO operation
    def callFileIO(self):
        f = FileIO()
        f.callingFIO()

    # method for calling all operations
    def AllOperationExecution(self):

        while True:
            print("\n\n"
                "Options->" "  1. Calculator" "\t\t2. Stack" "\t\t3. Single LinkList" "\t\t4. Double Link List" "\t\t5. Queue" "\t\t6. Sorting" "\t\t 7.File IO" "\t\t 8.exit\n")


            # getting User input

            press =int(input("Select and Enter The Number From Above option  \n\n"))

            # Depending on the user input method will call
            if press == 1:
                self.calExecution()

            elif press == 2:
                self.stackExecution()

            elif press == 3:
                self.singleLLExecution()

            elif press == 4:
                self.dLLExecution()

            elif press == 5:
                while True:
                    print("***Select the Queue Operation you want***\n"
                          "1.Simple Queue\n"
                          "2.Circular Queue\n"
                          "3.Exit\n")

                    enter = int(input("please enter the number"))

                    if enter == 1:
                        self.QueExecution()

                    elif enter == 2:
                        self.CirQueueExecution()
                    elif enter == 3:
                        print("Invalid Menu selected")
                        break

            elif press == 6:
                self.SortsExecution()

            elif press == 7:
                self.callFileIO()

            elif press == 8:
                print('Exited successfully')  # user will exit the process successfully
                break


q = Pythonmain()
q.AllOperationExecution()













