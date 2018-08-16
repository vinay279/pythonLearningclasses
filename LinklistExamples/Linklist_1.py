# class node for defining node
class Node:

    def __init__(self):
        self.data = None
        self.next = None

# class LinkList
class LinkedList:

    def __init__(self):
        self.head = None

    # inserting data in LinkList
    def insert(self, data):
        data = input("Add an element:")
        node = Node()
        node.data = data
        node.next = self.head
        self.head = node

    # printing data of from LinkList
    def print(self):
        print_list = self.head
        while print_list:
            print(print_list.data)
            print_list = print_list.next

    # printing size of the link list
    def size(self):
        i = 0
        head = self.head
        while head:
            i += 1
            head = head.next
        print(i)

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        return data
# creating object
MyList = LinkedList()

# for displaying data on the console
while True:
    print("1. Add an element")
    print("2. Print the list")
    print("3. Size of the list")
    print("4.pop item from list")
    menu = int(input("Choose an action:"))

    if menu == 1:
        MyList.insert(1)
    elif menu == 2:
        MyList.print()
    elif menu == 3:
        MyList.size()
    elif menu == 4:
        MyList.pop()
