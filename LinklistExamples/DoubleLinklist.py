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

    # method used for the taking input from user
    def operationDl(self):
        dllist = DoublyLinkedList()
        # display this on console
        print('Menu')
        print(" please write the sentences and in the angular brackets write the data and index you want")
        print('1.insert <data> after <index>')
        print('2.insert <data> before <index>')
        print('3.insert <data> at beg')
        print('4.insert <data> at end')
        print('5.remove <index>')
        print('6.quit')

        while True:
            print('The list: ', end='')
            dllist.display()
            print()
            do = int(input('What would you like to do? ').split())

            operation = do[0].strip().lower()

            # if user write insert operation of console
            if operation == '1':
                data = int(do[1])
                position = do[3].strip().lower()
                new_node = Node(data)
                suboperation = do[2].strip().lower()
                if suboperation == 'at':
                    if position == 'beg':
                        dllist.insert_at_beg(new_node)
                    elif position == 'end':
                        dllist.insert_at_end(new_node)
                else:
                    index = int(position)
                    ref_node = dllist.get_node(index)
                    if ref_node is None:
                        print('No such index.')
                        continue
                    if suboperation == 'after':
                        dllist.insert_after(ref_node, new_node)
                    elif suboperation == 'before':
                        dllist.insert_before(ref_node, new_node)

            # for remove operation written by user
            elif operation == 'remove':
                index = int(do[1])
                node = dllist.get_node(index)
                if node is None:
                    print('No such index.')
                    continue
                dllist.remove(node)

            elif operation == 'quit':
                break



