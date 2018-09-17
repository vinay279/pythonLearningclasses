'''Class for the Sorting Automation'''
import random
from SortingTypes import Bubble, Quick, Selection, Insertion, Radix, Merge
class SortingAutomation:
    def __init__(self):
        self.elements = []

    # Inserting Elements in List

    def inserting(self):
        for value in range(10):
            self.elements.append(random.randrange(1, 101))
        print("Elements list for Sorting =", self.elements)


    # Check the values in list and the length of list
    def checkValuesAndLength(self, elements, sample):
        if len(self.elements) == len(sample):
            for i in range(len(self.elements)):
                if self.elements[i] == sample[i]:
                    print("value are Equal in two list", self.elements[i], '=', sample[i])

                else:
                    print("Elements are not equal sorting fail")
                # for checking the total element list
        if len(self.elements) == len(sample):
            print("length of two sorted list is aso equal ")

        print("Test case of Soring passed", '\n')

    # for Clearing list
    def clearlist(self):
        self.elements.clear()


    # checking the Bubble sorting
    def checkBubbleSort(self):
        print("****Test case for Checking Bubble Sort****")
        self.clearlist()
        self.inserting()
        sample2 = self.elements
        bObj = Bubble.BubbleSort()
        bObj.BubbleSort(sample2)
        # check bubble sort after comaparing with selection sort
        csObj = Selection.Selection()
        csObj.selectionSort(self.elements)
        self.checkValuesAndLength(self.elements, sample2)
        print('*' * 70)


    def CheckSelectionSort(self):
        print("****Test case for Checking Selection Sort****")
        self.clearlist()
        self.inserting()
        sample2 = self.elements
        bObje = Selection.Selection()
        bObje.selectionSort(sample2)
        # check bubble sort after comaparing with selection sort
        buobj = Bubble.BubbleSort()
        buobj.BubbleSort(self.elements)

        self.checkValuesAndLength(self.elements,sample2)
        print('*' * 70)

    # for checking Quick sort is running
    def checkQuickSort(self):
        print("****Test case for Checking Quick Sort****")
        self.clearlist()
        self.inserting()
        sample2 = self.elements
        bobje = Selection.Selection()
        bobje.selectionSort(sample2)

        # check Quick sort after comaparing with selection sort
        Qobj = Quick.QuickS()
        Qobj.quickSort(self.elements)
        self.checkValuesAndLength(self.elements, sample2)
        print('*' * 70)

    # for Radix sort
    def checkRadixSort(self):
        print("****Test case for Checking Radix Sort****")
        self.clearlist()
        self.inserting()
        sample2 = self.elements
        Qsobj = Quick.QuickS()
        Qsobj.quickSort(self.elements)

        # check Quick sort after comaparing with selection sort
        Qobj = Radix.Radix()
        Qobj.radixSort(self.elements)
        self.checkValuesAndLength(self.elements, sample2)




    # checking insertion sort
    def checkingInsertionSort(self):
        print("****Test case for Insertion Bubble Sort****")
        self.clearlist()
        self.inserting()
        sample2 = self.elements
        Robj = Radix.Radix()
        Robj.radixSort(self.elements)

        # check radix sort after comaparing with insertion sort
        Qobj = Insertion.Insertion()
        Qobj.insertionSort(self.elements)
        self.checkValuesAndLength(self.elements, sample2)
        print('*' * 70)

    # checking the merge Sorting
    def checkMergeSorting(self):
        print("****Test case for Checking Merge Sort****")
        self.clearlist()
        self.inserting()
        sample2 = self.elements
        Robj = Radix.Radix()
        Robj.radixSort(self.elements)

        # check radix sort after comaparing with merge sort
        Qobj = Merge.Merge()
        Qobj.mergesort(self.elements)
        print("Merge Sorted list = ", self.elements)
        self.checkValuesAndLength(self.elements, sample2)
        print('*' * 70)


obj = SortingAutomation()
obj.checkBubbleSort()
obj.CheckSelectionSort()
obj.checkQuickSort()
obj.checkRadixSort()
obj.checkingInsertionSort()
obj.checkMergeSorting()