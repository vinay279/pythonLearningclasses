class StackUsingList:
    ''''the class is for the stack operation'''
    def __init__(self):
        self.stack = list()
        self.MAXSIZE= int(input('value from user '))
        self.top=0

    def push (self,data):
        if self.top >= self.MAXSIZE:
            print('Stack is full ')

        else:
            self.stack.append(data)
            self.top +=1

        # Removes element from the stack
    def pop(self):
            if self.top <= 0:
                return ("Stack Empty!")
            item = self.stack.del(s)
            self.top -= 1
            return item

        # Size of the stack
    def size(self):
            return self.top

s = StackUsingList()

