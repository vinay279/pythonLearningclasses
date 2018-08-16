class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
S1= Stack()

while True:
        print("1. Is stack is Empty")
        print("2. Push")
        print("3. pop")
        print("4. peek")
        print("5. size")
        menu = int(input("Choose an action:"))

        if menu == 1:
            S1.isEmpty()
        elif menu == 2:
            S1.push()
        elif menu == 3:
            S1.pop()
        elif menu == 4:
            S1.peek()
        elif menu == 5:
            S1.size()