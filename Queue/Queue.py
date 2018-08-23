#Queue Example using list
class Queue:
    itemlist = []
    def __init__(self,item):
        self.items=item

    def insert(self,item):
        int(input(print('Enter the number you want to append')))
        self.itemlist.append(self.item)
        print('your number is inserted in queue successfully')


    def remove(self):
        self.itemlist.pop(self)
q = Queue

while True:
    print("1. Append")
    print("2. Appendleft")
    print("3. pop")
    print("4. popleft")
    print("5. size")
    menu = int(input("Choose an action:"))

    if menu == 1:
        Queue.insert()

    elif menu == 2:
        Queue.remove()
