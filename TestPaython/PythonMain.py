import Sorting
from PythonLearningPractice import PythonClasses
from StackExample import Stack
from Calculator import Calculator
from LinklistExamples import *
from FileIO import *
from Sorting import BubbleSort,MergeSort,SelectionSort,InsertionSort

class PythonMain:
    ''' This class for doing all operation
        * calculator
        * stack
        * LinkList
        * Queue
        * File Operation '''

while True:

        print("1.Calculator")
        print("2.Stack")
        print("3.LinkList ")
        print("4.Queue")
        print("5.FileIO")
        print("6.sorting")
        menu = int(input("Choose an Operation you want to perform:"))

        if menu == 6:

            v1 = BubbleSort()
        elif menu == 2:
            s1 = Stack()


