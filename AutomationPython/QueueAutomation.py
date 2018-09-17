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
        self.queue.append(self.element+1)
        print("The first Element Added =", self.element+1)
        self.queue.append(self.element + 2)
        print("The second Element Added =", (self.element + 2))
        print("Now Queue contains =", self.queue)


    # Check Element is not present in Queue
    def checkElementnotPresent(self, element, sample):
        if self.element not in sample:
            print("Element is Not present in Queue Removed successfully")
        else:
            print("Element is present in list")
        print("Now Queue Contains after Removing  Element ", sample, '\n')


    # check insert operation in queue
    def checkInsertOperationinQueue(self):
        # by Using the Automation code
        print('\n')
        print("****Insert Operation using Queue Automation****")
        self.queue.clear()
        self.addElements()

        # Checking the inserted element is present in Queue
        if self.element+1 in self.queue:
            print("The Element is inserted ", self.element+1)
            print("Element is present in Queue")
        else:
            print("Element is Not present in list")
        print("Now Queue Contains  Last Inserted Element ", self.queue, '\n')

        # by Using the function written

        print("****Insert Operation Using Function****")
        q = Queue()
        print("Initially Queue Contains", q.queue)
        q.insert(self.element+1)
        q.insert(self.element + 2)
        print("Now the contents of queue is =", q.queue)

        # Checking the inserted element is present in Queue
        if self.element+1 in q.queue:
            print("The Element is inserted ", self.element+1)
            print("Element is present in Queue")
        else:
            print("Element is Not present in list")

        # comparing two Queues Are Equal or not
        AutomatedQueue = self.queue
        FunctionQueue = q.queue

        for QAelements in AutomatedQueue:
            for QFelements in FunctionQueue:
                if QAelements == QFelements:
                    None
        print("Both Queue are Same Insertion TestCase passed")
        print('*' * 70)

    # Removing  elements from the Queue
    def checkRemoveOperation(self):
        # by Using the Automation code
        print("\n")
        print("Test case for checking Remove Operation")
        self.queue.clear()
        self.addElements()
        print(" Element Remove from Queue ", self.queue.popleft())
        print("After Remove of Element Queue content = ", self.queue)

        # Checking the inserted element is present in Queue
        self.checkElementnotPresent(self.element, self.queue)

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
        self.checkElementnotPresent(self.element, q.queue)
        print('*' * 70)


    # checking size after insert
    def checkSizeAfterInsert(self):
        print('\n')
        print("**** Check Size After Insert Operation using Queue Automation****")
        self.queue.clear()
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
        print('*' * 70)


    def checkSizeAfterRemove(self):
        print('\n')
        print("**** Check Size After Insert Operation using Queue Automation****")
        self.queue.clear()
        self.addElements()
        print(" Element Remove from Queue ", self.queue.popleft())
        print("After Remove of Element Queue content = ", self.queue)

        # finding size
        size = 0
        for elements in self.queue:
            size += 1
        print("Size of Queue Is = ", size)

        # by using the function
        print("**** Operation Using Function****")
        q = Queue()
        print("Initially Queue Contains", q.queue)
        q.insert(self.element + 1)
        q.insert(self.element + 2)
        q.remove()
        print("Now Queue Contains", q.queue)

        # calling function of size from the
        q.size()

        if q.size() == size:
            print("both sizes of Queue are Equal Test Case passed")

        else:
            print("Test Case is Failed size is not Equal")

        print('*' * 70)

    def checkRemoveFromEmptyQueue(self):
        print('\n')
        print("Test case for checking Deleting from Empty Queue")
        self.queue.clear()
        print('Now Queue contains', self.queue)

        print('Trying to Delete from Empty Queue')
        try:
            self.queue.popleft()
        except IndexError:
            print("You cant Remove from Empty Queue")
        print("Test Case is Passed")

        print('*'*71)

m = AutomateQueue()
m.checkInsertOperationinQueue()
m.checkRemoveOperation()
m.checkRemoveFromEmptyQueue()
m.checkSizeAfterInsert()
m.checkSizeAfterRemove()