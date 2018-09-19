''' This class is used for '''


class Stack:
    def __init__(self):
        self.items = [10, 3]

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
        print("data is pushed successfully", data)
        print('Stack contains data after push', self.items)


    def pop(self):
        try:
            self.items.pop()
            print('Stack contains data after pop', self.items)
        except IndexError:

            print("You cant POP from Empty list")


    def size(self):
        return print('size of stack after push', len(self.items)-1)

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



