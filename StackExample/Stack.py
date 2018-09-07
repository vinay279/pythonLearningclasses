''' This class is used for '''


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
        print("data is added successfully",self.items)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)-1

    def callingStack(self):

        while True:
            print('\t1.push ')
            print('\t2.pop')
            print('\t3.Display Stack')
            print('\t4.Quit')
            operation = int(input('What would you like to do? '))

            if operation == 1:
                data = input("enter data u want to push")
                self.push(data)
                print("data push successfully",data)

            elif operation == 2:
                if self.is_empty():
                    print('Stack is empty.')
                else:
                    print('Popped value: ', self.pop())
            elif operation == 3:
                print(self.items)

            elif operation == 4:
                print("successfully exited")
                break
            else:
                print("Invalid Input Please Enter Correct")



