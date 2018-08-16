# importing "collections" for deque operations
import collections
from datetime import date


class Queue:

    def __init__(self):
        self.items.collections.deque([])

    def append(self, item):
        self.items.collections.deque.append(item)

    def appendleft(self, item):
        self.items.collections.deque.appendleft(item)

    def pop(self):
        return self.items.collections.dequepop()

    # for pop left item
    def popleft(self):
        return self.items.collections.dequepopleft()

    def size(self):
        return len(self.items.collections.deque)

Queue = Queue()

while True:
    print("1. Append")
    print("2. Appendleft")
    print("3. pop")
    print("4. popleft")
    print("5. size")
    menu = int(input("Choose an action:"))

    if menu == 1:
        Queue.append()
    elif menu == 2:
        Queue.apendleft()
    elif menu == 3:
        Queue.pop()
    elif menu == 4:
        Queue.popleft()
    elif menu == 5:
        Queue.size()