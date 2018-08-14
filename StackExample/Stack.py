class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def length(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    print("Please select operation -\n" \
          "1. push\n" \
          "2. pop\n" \
          "3. length\n" \
          "4. IsEmpty\n")

    # Take input from the user
                s=Stack()
        select = input("Select operations form 1, 2, 3, 4 :")

    Input = str(input("Enter the input: "))
    if select == '1':
        push(Input)
        print("Data is pushed successfully")

    elif select == '2':
            pop(Input)
            print("Data is pop successfully")

    elif select == '3':
            print('Length is ', length())

    elif select == '4':
        print('Is the stack is empty')
    else:
        print("Invalid input")