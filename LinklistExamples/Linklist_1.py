'''
   This class is performing the link list Operations such as
        'insert <data> after <index>  any node'
        'insert <data> before <index> any  Node of link list'
        'insert <data> at beginning of link list'
        'insert <data> at end of link list'
        'remove Node <index>'   '''




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class for the linklist operation getnode,insert after , insert before , insert at beginning
# and insert at the end
class LinkedList:
    def __init__(self):
        self.head = None

    # method use for getting node
    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    # method use for the getting previous node
    def get_prev_node(self, ref_node):
        current = self.head
        while current and current.next != ref_node:
            current = current.next
        return current

    # method used for the insert the node after the node
    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node

    # method used for the insert the node before
    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)

    # method used for the insert the node at beginning
    def insert_at_beg(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # method used for the insert the node at the end
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # method for the remove node from linklist
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    # method for the display nodes from linklist
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    # method for the purpose of calling the function from the

    def operationsLL(self):
        # display this on console
        print('1.Insert data at beginning')
        print('2.Insert data at end')
        print('3.Insert data after index')
        print('4.Insert data before index')
        print('5.Remove Node')
        print('6.Display LinkList')
        print('7.Quit')

        while True:

            do = int(input('What would you like to do? '))

            # insert at beg
            if do == 1:
                data = input("Enter Data")
                new_node = Node(data)
                self.insert_at_beg(new_node)

            # insert at end
            elif do == 2:
                data = input("Enter Data")
                new_node = Node(data)
                self.insert_at_end(new_node)

            # insert after
            elif do == 3:
                index = int("eneter Index")
                ref_node = self.get_node(index)
                if ref_node is None:
                    print('No such index.')

                else:
                    data = input("Enter Data")
                    new_node = Node(data)
                    self.insert_after(ref_node, new_node)

            # insert before
            elif do == 4:
                index = int("eneter Index")
                ref_node = self.get_node(index)
                if ref_node is None:
                    print('No such index.')

                else:
                    data = input("Enter Data")
                    new_node = Node(data)
                    self.insert_before(ref_node, new_node)

            elif do == 5:
                index = int(input("Enter Index you want to Remove"))
                node = self.get_node(index)
                if node is None:
                    print('No such index.')
                    continue
                self.remove(node)

            elif do == 6:
                print('The list: ', end='')
                self.display()
                print()

            elif do == 7:
                print("Exited Successfully")
                break

            else:
                print("Inavalid input please enter correct")