''' class for simple Queue Operations
    1. Insert into Queue
    2. Delete from the Queue
    3. Reset Queue

'''


class Queue:

    # Constructor
    def __init__(self):
        self.queue = list()
        self.maxSize = 9999
        self.head = 0
        self.tail = 0

    # Adding elements
    def insert(self, data):
        # Checking if the queue is full
        if self.size() >= self.maxSize-1:
            return (" Queue Full ")
        self.queue.append(data)
        self.tail += 1
        return True

        # Deleting elements
    def remove(self):
        # Checking if the queue is empty
        if self.size() <= 0:  # checking the size of queue
            self.resetQueue()
            return (" Queue Empty ")
        data = self.queue[self.head]
        if data is 0:
            print("Queue is empty you can't delete")
        self.head += 1
        print(' Data is removed successfully and You can see Zero at the position of this data', self.queue[self.head-1])
        self.queue[self.head-1] = 0
        return data

    # Calculate size
    def size(self):
        count = int(self.tail - self.head) # getting the size of
        return count

    # Reset queue
    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()

    def callingQueue(self):
        while True:
            print('1.Insert to Queue')
            print('2.Remove from Queue')
            print('3.Display Queue')
            print('4.Reset Queue')
            print('5.Exit')
            operation = int(input('What would you like to do? '))

            if operation == 1:
                data = input("Enter the values ou want to insert in the Queue")
                self.insert(data)
                print("Data Is Inserted Successfully",data)

            elif operation == 2:
                self.remove()

            elif operation == 3:
                print("Queue contains Data = ", self.queue)

            elif operation == 4:
                print("Queue reseted successfully ", self.resetQueue)

            elif operation == 5:
                print('Exited successfully')  # user will exit the process successfully
                break

            else:
                print("Invalid operation Please Enter correct Option")

