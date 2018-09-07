'''
   This class is performing the Double linkList Operations such as
        'insert <data> after <index>  any node'
        'insert <data> before <index> any  Node of link list'
        'insert <data> at beginning of link list'
        'insert <data> at end of link list'
        'remove Node <index>'   '''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# class for the linklist operation getnode,insert after , insert before , insert at begining
# and insert at the end

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    # method use for getting node

    def get_node(self, index):
        current = self.first
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    # method used for the insert the node after the node
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        if ref_node.next is None:
            self.last = new_node
        else:
            new_node.next = ref_node.next
            new_node.next.prev = new_node
        ref_node.next = new_node

    def insert_before(self, ref_node, new_node):
        new_node.next = ref_node
        if ref_node.prev is None:
            self.first = new_node
        else:
            new_node.prev = ref_node.prev
            new_node.prev.next = new_node
        ref_node.prev = new_node

    # method used for the insert the node at beginning
    def insert_at_beg(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.insert_before(self.first, new_node)

    # method used for the insert the node at the end
    def insert_at_end(self, new_node):
        if self.last is None:
            self.last = new_node
            self.first = new_node
        else:
            self.insert_after(self.last, new_node)

    # method used for the remove node from the link list
    def remove(self, node):
        if node.prev is None:
            self.first = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev

    # method used for display all node
    def display(self):
        current = self.first
        while current:
            print(current.data, end=' ')
            current = current.next

    # method used for the taking input from use

    def operationDl(self):
        # display this on console
        print('1.Insert data at beginning')
        print('2.Insert data at end')
        print('3.Insert data after index')
        print('4.Insert data before index')
        print('5.Remove Node')
        print('6.Display LinkList')
        print('7.Quit')

        while True:

            do = int(input("Select the input you want"))

            if do == 1:  # inserting data at beg
                data = input("Enter the data you want to insert")
                new_node = Node(data)
                self.insert_at_beg(new_node)

            elif do == 2:  # insert data at end
                data = input("Enter the data you want to insert")
                new_node = Node(data)
                self.insert_at_end(new_node)

            # insert data after index
            elif do == 3:
                data = input(" Enter Data")
                index = int(input("Enter the Index"))
                ref_node = self.get_node(index)
                if ref_node is None:
                    print('No such index.')

                else:
                    new_node = Node(data)
                    self.insert_after(ref_node, new_node)

            # insert data before index
            elif do == 4:
                data = input(" Enter Data")
                index = int(input("Enter the Index"))
                ref_node = self.get_node(index)
                if ref_node is None:
                    print('No such index.')

                else:
                    new_node = Node(data)
                    self.insert_before(ref_node, new_node)

            # remove node for the list
            elif do == 5:
                index = int(input(" Enter the index You want to Delete"))
                node = self.get_node(index)
                if node is None:
                    print('No such index.')
                    continue
                self.remove(node)

            # for display list
            elif do == 6:
                print('The list: ', end='')
                self.display()
                print()

            # exit operation
            elif do == 7:
                print("Exited Successfully")
                break

            else:
                print("Invalid input please enter correct")







