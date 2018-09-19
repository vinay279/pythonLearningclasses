'''this class is doing circular queue operation
        1. Insert into Queue
        2. Delete from the Queue
        3. Reset Queue '''

class CQueue:
    ''' Constructor '''

    def __init__(self):
        self.limit = 9999
        self.queue = []
        self.front = -1
        self.rear = -1

# method for remove the element from list
    def remove(self):
        if self.rear == -1:  # checking Queue is empty or not
            print('Queue is empty you can not remove Data')

        else:
            item = self.queue[self.front]
            self.queue[self.front] = 0
            self.front += 1
            print("Data is Remove Queue = ", item)
            if self.front == self.rear:
                self.front = -1
                self.rear = -1

            else:
                if self.front > self.limit:
                    p = self.front % self.limit
                    self.front = p - 1
            return item

# method used for the insertion operation of element in queue
    def insert(self, item):
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue.append(item)
        else:
            self.rear += 1
            if self.rear > self.limit:
                p = self.rear % self.limit
                self.rear = p - 1
                if self.rear < self.front:
                    self.queue.insert(self.rear, item)
                else:
                    print('queue is full')
            else:
                if self.rear == self.front:
                    self.rear -= 1
                    self.queue.insert(self.rear, item)
                else:
                    self.queue.append(item)

    def displayQueue(self):
        print(self.queue)

    def resetQueue(self):
        self.rear = 0
        self.front = 0
        self.queue = list()

# method use for the calling purpose of Circular queue

    def callingCQueue(self):
        while True:
            print('1.Insert to Queue')
            print('2.Remove from Queue')
            print('3.Reset Queue')
            print('4.Display Queue')
            print('5.Exit ')
            operation = int(input('What would you like to do? '))

            if operation == 1:
                data = input("Enter the values ou want to insert in the Queue\n")
                self.insert(data)
                print(" Data is Inserted Successfully ", data)

            elif operation == 2:
                self.remove()

            elif operation == 3:
                print("Queue is Reset sucessfully", self.resetQueue)

            elif operation == 4:
                self.displayQueue()

            elif operation == 5:
                print('Exited successfully')  # user will exit the process successfully
                break
            else:
                print("Invalid Input Please Enter Correct Input")


