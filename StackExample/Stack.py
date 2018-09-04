class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return self.items.__sizeof__()

    def callingStack(self):
        s = Stack()
        while True:
            print('1.push ')
            print('2.pop')
            print('3.size')
            print('4.quit')
            operation = int(input('What would you like to do? '))

            if operation == 1:
                data = input("enter data u want to push")
                s.push(data)

            elif operation == 2:
                if s.is_empty():
                    print('Stack is empty.')
                else:
                    print('Popped value: ', s.pop())
            elif operation == 3:
                s.size()

            elif operation == 4:
                print("successfully exited")
                break

            elif operation != 1 or operation != 2 or operation != 3 or operation != 4:
                print("invalid input please enter correct value")



