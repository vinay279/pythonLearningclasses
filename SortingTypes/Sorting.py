'''
         This class is perform six types of sorting
                1] Bubble Sort
                2] Selection Sort
                3] Insertion Sort
                4] Quick Sort
                5] Merge Sort
                6] Radix Sort                           '''
from SortingTypes import Merge,Radix,Insertion,Selection,Bubble,Quick
class Sorting:


    # Implementation for the user input
    # Options provided to the user

    def callSorting(self):
        while True:
            print("\t1.Bubble Sort\n"
                  "\t2.Selection Sort\n"
                  "\t3.Insertion Sort\n"
                  "\t4.Merge sort\n"
                  "\t5.Quick Sort\n"
                  "\t6.Radix Sort\n"
                  "\t7.Exit the Process ")

            menu = int(input(print("*******Select the sorting option You want to sort*******\n")))

            # if press 1 then user will get the bubble sort output

            if menu == 1:
                sample = [int(x) for x in
                          input("=>Please enter the values with spaces you want to Bubble Sort   :").split()]
                Bubble.BubbleSort.BubbleSort(sample) # calling bubble Sort method

            elif menu == 2:
                sample = [int(x) for x in
                          input(" =>Please enter the values with spaces you want to Selection Sort :  ").split()]

                self.selectionSort(sample)  # calling Selection sort method

            elif menu == 3:
                sample = [int(x) for x in
                          input("=>Please enter the values with spaces you want to Insertion Sort :").split()]

                self.insertionSort(sample)  # Calling insertion sort method

            elif menu == 4:
                sample = [int(x) for x in
                          input("=>Please enter the values with spaces you want to Merge Sort :").split()]

                self.mergesort(sample)  # Calling insertion sort method

            elif menu == 5:
                sample = [int(x) for x in input("=>Please enter the values with spaces you want to Sort :").split()]

                self.quickSort(sample)  # Calling Quick sort method

            elif menu == 6:
                sample = [int(x) for x in input("=>Please enter the values with spaces you want to Sort :").split()]

                self.radixSort(sample)  # Calling Radix sort method

            elif menu == 7:
                print('Exited successfully')  # user will exit the process successfully
                break

            else:
                print("Invalid Operation ")
