class Queue:

    # Constructor
    def __init__(self):
        self.queue = list()
        self.maxSize = int(input("enter the size of queue"))
        self.head = 0
        self.tail = 0

    # Adding elements
    def insert(self, data):
        # Checking if the queue is full
        if self.size() >= self.maxSize-1:
            return (" Queue Full ")
        self.queue.append(data)
        self.tail += 1
        print("value Inserted successfully")
        print('***'*9)

        return True

        # Deleting elements
    def remove(self):
        # Checking if the queue is empty
        if self.size() <= 0:
            self.resetQueue()
            return (" Queue Empty ")
        data = self.queue[self.head]
        if data is 0:
            print("Queue is empty you can't delete")
        self.head += 1
        print(' Data is removed successfully',self.queue[self.head-1])
        return data

    # Calculate size
    def size(self):
        count = int(self.tail- self.head)
        return count

    # Reset queue
    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()


q = Queue()
while True:
    print('1.Insert to Queue')
    print('2.Remove from Queue')
    print('4.Quit')
    operation = int(input('What would you like to do? '))

    if operation == 1:
        data = input("Enter the values ou want to insert in the Queue")
        q.insert(data)

    elif operation == 2:
        q.remove()

    elif operation == 3:
        q.size()

    elif operation == 4:
        print("successfully exited",q.resetQueue)
        break

    elif operation != 1 or operation != 2 or operation != 3 or operation != 4:
        print("invalid input please enter correct value")