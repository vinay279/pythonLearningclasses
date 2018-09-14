'''this class is used for the Queue Automation'''
#Importing the library
from collections import deque
import random
from Queue.Queue import Queue

class AutomateQueue:
    # method for automating queue
    def __init__(self):
        self.queue = deque([])
        self.element = random.randint(0, 99)


    # Enqueuing elements to the Queue

    def addElements(self):
        print("Initially Queue contains =", self.queue)
        print("The first Element Added =", (self.element + 1))
        self.queue.append(self.element + 1)
        print("The second Element Added =", (self.element + 2))
        self.queue.append(self.element + 2)
        print("Now Queue contains =", self.queue)

    def checkInsertOperation(self):

        # by Using the Automation code
        print('\n')
        print("****Insert Operation using Queue Automation****")
        self.addElements()
        self.queue.append(self.element)  # random element is appended
        print("After Insertion of Element Queue content = ", self.queue)


        # Checking the inserted element is present in Queue
        if self.element in self.queue:
            print("The Element is inserted ", self.element)
            print("Element is present in Queue")
        else:
            print("Element is Not present in list")
        print("Last Inserted Element Remove from Queue ", self.queue.pop())
        print("Now Queue Contains after Removing Last Inserted Element ",self.queue, '\n')


        # by Using the function written

        print("****Insert Operation Using Function****")
        q = Queue()
        print("Initially Queue Contains", q.queue)
        q.insert(self.element+1)
        q.insert(self.element + 2)
        print("Now the contents of queue is =", q.queue)
        q.insert(self.element)
        print("Now Queue Contains", q.queue)

        # Checking the inserted element is present in Queue
        if self.element in q.queue:
            print("The Element is inserted ", self.element)
            print("Element is present in Queue")
        else:
            print("Element is Not present in list")
        print("Last Inserted Element Remove from Queue ", q.queue.pop())
        print("Now Queue Contains after Removing Last Inserted Element ", q.queue, '\n')

        # comparing two Queues Are Equal or not
        AutomatedQueue = self.queue
        FunctionQueue = q.queue

        for QAelements in AutomatedQueue:
            for QFelements in FunctionQueue:
                if QAelements == QFelements:
                    print(QAelements)
        print("Both Queue are Same Insertion TestCase passed")


        # Removing  elements from the Queue
    def checkRemoveOperation(self):
        # by Using the Automation code
        print('\n')
        print("**** Remove Operation using Queue Automation****")
        print("Initially Queue contains =", self.queue)
        print("The first Element Added =", (self.element + 1))
        self.queue.append(self.element + 1)
        print("The second Element Added =", (self.element + 2))
        self.queue.append(self.element + 2)
        print("Now Queue contains =", self.queue)
        print(" Element Remove from Queue ", self.queue.popleft())
        print("After Remove of Element Queue content = ", self.queue)

        # Checking the inserted element is present in Queue
        if self.element not in self.queue:
            print("The Element is Remove = ", self.element)
            print("Element is Not present in Queue")
        else:
            print("Element is present in list")
        print("Now Queue Contains after Removing Last Inserted Element ", self.queue, '\n')

        # by Using the function written

        print("****Insert Operation Using Function****")
        q = Queue()
        print("Initially Queue Contains", q.queue)
        q.insert(self.element + 1)
        q.insert(self.element + 2)
        print("Now Queue Contains", q.queue)
        print(" Element Remove from Queue ", q.remove())
        print("Now Queue Contains", q.queue)


        # Checking the Removed element is present in Queue
        if self.element not in q.queue:
            print("Element is Not present in Queue Removed successfully")
        else:
            print("Element is present in list")
        print("Now Queue Contains after Removing  Element ", q.queue, '\n')


    # checking size after insert
    def checkSizeAfterInsert(self):
        print('\n')
        print("**** Check Size After Insert Operation using Queue Automation****")
        self.addElements()
        size = 0
        # finding size
        for elements in self.queue:
            size += 1
        print("Size of Queue Is = ", size)

        # by using the function

        print("****Insert Operation Using Function****")
        q = Queue()
        print("Initially Queue Contains", q.queue)
        q.insert(self.element + 1)
        q.insert(self.element + 2)
        print("Now Queue Contains", q.queue)

        # calling function of size from the
        q.size()


        if q.size() == size:
            print("both sizes of Queue are Equal Test Case passed")

        else:
            print("Test Case is Failed size is not Equal")


    def checkSizeAfterRemove(self):

        print('\n')
        print("**** Check Size After Insert Operation using Queue Automation****")
        self.addElements()
        print(" Element Remove from Queue ", self.queue.popleft())
        print("After Remove of Element Queue content = ", self.queue)

        size = 0
        # finding size
        for elements in self.queue:
            size += 1
        print("Size of Queue Is = ", size)

        # by using the function

        print("****Insert Operation Using Function****")
        q = Queue()
        print("Initially Queue Contains", q.queue)
        q.insert(self.element + 1)
        q.insert(self.element + 2)
        q.insert(self.element + 3)
        q.remove()
        print("Now Queue Contains", q.queue)

        # calling function of size from the
        q.size()

        if q.size() == size:
            print("both sizes of Queue are Equal Test Case passed")

        else:
            print("Test Case is Failed size is not Equal")

        pass

    def checkRemoveFromEmptyQueue(self):

        print('now Queue contains', self.queue)
        try:
            self.queue.popleft()
        except IndexError:
            print("You cant Remove from Empty Queue")


m = AutomateQueue()
m.checkInsertOperation()