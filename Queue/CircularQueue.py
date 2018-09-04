class CQueue():
    ''' Constructor '''

    def __init__(self, limit):
        self.limit = limit
        self.queue = list()
        self.front = -1
        self.rear = -1

    def remove(self):
        if self.rear == -1:
            print('queue is empty')

        else:
            item = self.queue[self.front]
            self.front += 1
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                if self.front > self.limit:
                    p = self.front % self.limit
                    self.front = p - 1
            return item

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

q = CQueue(int(input("enter the size of cicular Queue")))
while True:
    print('1.Insert to Queue')
    print('2.Remove from Queue')
    print('3.Quit')
    operation = int(input('What would you like to do? '))

    if operation == 1:
        data = input("Enter the values ou want to insert in the Queue")
        q.insert(data)

    elif operation == 2:
        q.remove()

    elif operation == 3:
        print("successfully exited", q.resetQueue)
        break

    elif operation != 1 or operation != 2 or operation != 3 or operation != 4:
        print("invalid input please enter correct value")