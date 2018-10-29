'''class for creating binary tree'''
class BinaryTree:
    TreeData = []

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data: # check data

                if self.left is None:
                    self.left = BinaryTree(data)
                    print(self.data, 'is parent and left child is ', data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                    print(self.data, 'is parent and  right child is ', data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Inorder traversal
    # Left -> Root -> Right

    def inOrderTraversalAndSortedData(self, root):

        if root:
            self.inOrderTraversalAndSortedData(root.left)
            print(root.data)
            self.inOrderTraversalAndSortedData(root.right)


    def printing(self,treeData,root):

        for val in range(1, len(treeData)-1):
            root.insert(treeData[val])
        print('\n')

    def updateBinaryTree(self, valToBeInsert):
        b = BinaryTree(self.TreeData[0])
        b.TreeData.append(int(valToBeInsert))
        for val in b.TreeData:
            self.insert(val)
        self.printing(valToBeInsert,  b.TreeData)

    def Searching(self,data,treeData):
        if data in treeData:
            print(data)

        else:
            print('Data is Not Present In Tree')

    def enterData(self):
        treeData = [int(x) for x in input("=>Please enter the values with spaces you want  :").split()]
        obj = BinaryTree(1)
        for val in treeData:
            obj.TreeData.append(val)
        return treeData


    def callingFunctions(self):

        while True:
            print("\t1.Create Tree\n"
                  "\t2.Update Node in Tree\n"
                  "\t3.Delete Node in Tree\n"
                  "\t4.InOrder Traversing of Tree\n"
                  "\t5.Sorting of Tree\n"           
                  "\t6.Exit \n")


            menu = int(input("*******Select the sorting option You want to sort*******\n"))

            if menu == 1:
                self.TreeData = [int(x) for x in input("=>Please enter the values with spaces you want  :").split()]

                root = BinaryTree(self.TreeData[0])
                print("Root is ", self.TreeData[0], 'and it is parent ')
                root.printing(self.TreeData,root)


            elif menu == 2:
                root = BinaryTree(self.TreeData[0])
                valToBeInsert = input("Enter value to be Insert => ")
                self.TreeData.append(valToBeInsert)
                root = BinaryTree(self.TreeData[0])
                print("Root is ", self.TreeData[0], 'and it is parent ')
                root.printing(self.TreeData, root)

            elif menu == 3:
                root = self.TreeData[0]
                self.inOrderTraversalAndSortedData(root)

            elif menu == 4:
                root.inOrderTraversalAndSortedData(root)


c = BinaryTree()
c.callingFunctions()