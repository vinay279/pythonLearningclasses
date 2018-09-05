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

# class for the linklist operation getnode,insert after , insert before , insert at begining
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
        while (current and current.next != ref_node):
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
        a_llist = LinkedList()

        print('Menu')
        print(" please write the sentences and in the angular brackets write the data and index you want")
        print('insert <data> after <index>')
        print('insert <data> before <index>')
        print('insert <data> at beg')
        print('insert <data> at end')
        print('remove <index>')
        print('quit')

        while True:
            print('The list: ', end='')
            a_llist.display()
            print()
            do = input('What would you like to do? ').split()

            operation = do[0].strip().lower()

            if operation == 'insert':
                data = int(do[1])
                position = do[3].strip().lower()
                new_node = Node(data)
                suboperation = do[2].strip().lower()
                if suboperation == 'at':
                    if position == 'beg':
                        a_llist.insert_at_beg(new_node)
                    elif position == 'end':
                        a_llist.insert_at_end(new_node)
                else:
                    index = int(position)
                    ref_node = a_llist.get_node(index)
                    if ref_node is None:
                        print('No such index.')
                        continue
                    if suboperation == 'after':
                        a_llist.insert_after(ref_node, new_node)
                    elif suboperation == 'before':
                        a_llist.insert_before(ref_node, new_node)

            elif operation == 'remove':
                index = int(do[1])
                node = a_llist.get_node(index)
                if node is None:
                    print('No such index.')
                    continue
                a_llist.remove(node)

            elif operation == 'quit':
                break

