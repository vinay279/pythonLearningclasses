'''Class for the Sorting Automation'''
import random
from SortingTypes import Bubble,Quick,Selection,Insertion,Radix,Merge
class SortingAutomation:
    def __init__(self):
        self.elements = []

    # checking the Bubble sorting
    def checkBubbleSort(self):


        for value in range(10):
            self.elements.append(random.randrange(1, 101))
        print(self.elements)

        sample2 = self.elements
        bObj = Bubble.BubbleSort()
        bObj.BubbleSort(sample2)
        # check bubble sort after comaparing with selection sort
        csObj = Selection.Selection()
        csObj.selectionSort(self.elements)


        for values in self.elements:
            for element in sample2:
                if values == element:
                        None
            print("Bubble sort Test Case passed")
            break
        else:
            print("Test case of Bubble sort is failed is failed")

        # for checking the total element list
        if len(self.elements) == len(sample2):
                print("length is also equal ")


    def CheckSelectionSort(self):
        for value in range(10):
            self.elements.append(random.randrange(1, 101))

        sample2 = self.elements
        bObje = Selection.Selection()
        bObje.selectionSort(sample2)
        # check bubble sort after comaparing with selection sort
        buobj = Bubble.BubbleSort()
        buobj.BubbleSort(self.elements)

        if len(self.elements) == len(sample2):
            for i in range(len(self.elements)):
                if self.elements[i] == sample2[i]:
                    print("value are Equal in two list", self.elements[i], '=', sample2[i])

                else:
                    print("Elements are not equal Selection sorting fails")
        print("Test case of Selection Soring passed")

    # for checking Quick sort is running
    def checkQuickSort(self):
        for value in range(10):
            self.elements.append(random.randrange(1, 101))
        print(self.elements)

        sample2 = self.elements
        bobje = Selection.Selection()
        bobje.selectionSort(sample2)

        # check Quick sort after comaparing with selection sort
        Qobj = Quick.QuickS()
        Qobj.quickSort(self.elements)

        if len(self.elements) == len(sample2):
            for i in range(len(self.elements)):
                if self.elements[i] == sample2[i]:
                    print("value are Equal in two list", self.elements[i], '=', sample2[i])

                else:
                    print("Elements are not equal Quick sorting fails")


        # for checking the total element list
        if len(self.elements) == len(sample2):
            print("length is also equal ")

        print("Test case of Quick Soring passed")

    # for Radix sort
    def checkRadixSort(self):
        for value in range(10):
            self.elements.append(random.randrange(1, 101))
        print(self.elements)

        sample2 = self.elements
        Qsobj = Quick.QuickS()
        Qsobj.quickSort(self.elements)

        # check Quick sort after comaparing with selection sort
        Qobj = Radix.Radix()
        Qobj.radixSort(self.elements)

        if len(self.elements) == len(sample2):
            for i in range(len(self.elements)):
                if self.elements[i] == sample2[i]:
                    print("value are Equal in two list", self.elements[i], '=', sample2[i])

                else:
                    print("Elements are not equal radix sorting fails")


        # for checking the total element list
        if len(self.elements) == len(sample2):
            print("length of two sorted list is aso equal ")

        print("Test case of radix  Soring passed")

    # checking insertion sort
    def checkingInsertionSort(self):
        for value in range(10):
            self.elements.append(random.randrange(1, 101))
        print(self.elements)

        sample2 = self.elements
        Robj = Radix.Radix()
        Robj.radixSort(self.elements)

        # check radix sort after comaparing with insertion sort
        Qobj = Insertion.Insertion()
        Qobj.insertionSort(self.elements)

        if len(self.elements) == len(sample2):
            for i in range(len(self.elements)):
                if self.elements[i] == sample2[i]:
                    print("value are Equal in two list", self.elements[i], '=', sample2[i])

                else:
                    print("Elements are not equal Insertion sorting fails")


        # for checking the total element list
        if len(self.elements) == len(sample2):
            print("length of two sorted list is aso equal ")

        print("Test case of Insertion  Soring passed")

    # checking the merge Sorting
    def checkMergeSorting(self):
        for value in range(10):
            self.elements.append(random.randrange(1, 101))
        print("List to be Sorted is = ", self.elements)

        sample2 = self.elements
        Robj = Radix.Radix()
        Robj.radixSort(self.elements)

        # check radix sort after comaparing with merge sort
        Qobj = Merge.Merge()
        Qobj.mergesort(self.elements)
        print("Merge Sorted list = ", self.elements)

        if len(self.elements) == len(sample2):
            for i in range(len(self.elements)):
                if self.elements[i] == sample2[i]:
                    print("value are Equal in two list", self.elements[i], '=', sample2[i])

                else:
                    print("Elements are not equal Insertion sorting fails")


        # for checking the total element list
        if len(self.elements) == len(sample2):
            print("length of two sorted list is aso equal ")

        print("Test case of Insertion  Soring passed")


clsObj = SortingAutomation()
clsObj.checkMergeSorting()