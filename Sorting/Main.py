'''
         This class is perform six types of sorting
                1] Bubble Sort
                2] Selection Sort
                3] Insertion Sort
                4] Quick Sort
                5] Merge Sort
                6] Radix Sort                           '''

class Sorting:

    # Constructor of the class for defining instance variable

    def __init__(self, samplelist):
        self.samplelist = samplelist

    #  Bubble sort
    #  Statement:
    #  Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
    #  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
    #
    # Time Complexity of Solution:
    #  Best O(n^2); Average O(n^2); Worst O(n^2).
    #
    #  Approach:
    #   Bubblesort is an elementary sorting algorithm. The idea is to
    #   imagine bubbling the smallest elements of a (vertical) array to the
    #   top; then bubble the next smallest; then so on until the entire
    #   array is sorted. Bubble sort is worse than both insertion sort and
    #   selection sort. It moves elements as many times as insertion sort
    #   (bad) and it takes as long as selection sort (bad). On the positive
    #   side, bubble sort is easy to understand. Also there are highly
    #   improved variants of bubble sort.
    #
    # Step 1 - For each element at index i from 0 to n, loop:
    # Step 2 - For each element at index k, from n to i exclusive, loop:
    # Step 3 - If the element at k is less than that at k-1, swap them.
    # =======================================================================

    def BubbleSort(self, samplelist):
        length = len(samplelist)
        for outer in range(length - 1):  # for tracing the list from start to end
            for inner in range(length - 1 - outer):  # it will skip the last element which is already sorted
                if samplelist[inner] > samplelist[inner + 1]:  # comparing two elements
                    samplelist[inner], samplelist[inner + 1] = samplelist[inner + 1], samplelist[
                        inner]  # swapping two element

        print(' All values bubble sorted successfully =>', samplelist)  # printing the sorted list

    # =======================================*****==================================================


    # Selection Sort

    #  method performing Selection Sort operation
    #  Statement:
    #  Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [18,5,3,1,19,6,0,7,4,2,5]
    #  Sample Output: [0,1,2,3,4,5,5,6,7,18,19]
    #
    #  Time Complexity of Solution:
    #  Best O(n^2); Average O(n^2); Worst O(n^2).
    #
    #  Approach:
    # Step 1 − Set MIN to location 0
    # Step 2 − Search the minimum element in the list
    # Step 3 − Swap with value at location MIN
    # Step 4 − Increment MIN to point to next element
    # Step 5 − Repeat until list is sorted



    def selectionSort(self, samplelist):
        for fillslot in range(len(samplelist) - 1, 0, -1):
            positionOfMax = 0
            for location in range(1, fillslot + 1):
                if samplelist[location] > samplelist[positionOfMax]:
                    positionOfMax = location

            temp = samplelist[fillslot]
            samplelist[fillslot] = samplelist[positionOfMax]
            samplelist[positionOfMax] = temp

        print('sorted values are : ', samplelist)

    #=======================================*****==================================================

    # Insertion Sort
    #  Statement:
    #  Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
    #  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
    #
    #  Time Complexity of Solution:
    #  Best O(n); Average O(n^2); Worst O(n^2).
    #
    # Approach:
    # Step 1 − Get a list of unsorted numbers.
    # Step 2 − Set a marker for the sorted section after the first number in the list.
    # Step 3 − Repeat steps 4 through 6 until the unsorted section is empty.
    # Step 4 − Select the first unsorted number.
    # Step 5 − Swap this number to the left until it arrives at the correct sorted position.
    # Step 6 − Advance the marker to the right one position.
    # Step 7 − Stop.

    # Method performing the insertion sort

    def insertionSort(self, samplelist):
        for index in range(1, len(samplelist)):
            tmp = samplelist[index]
            k = index
            while k > 0 and tmp < samplelist[k - 1]:
                samplelist[k] = samplelist[k - 1]
                k -= 1
            samplelist[k] = tmp
        print("The given list is sorted suceesfully  as :", samplelist)

    # =======================================*****==================================================


    #@@ Merge Sort

    #  Statement:
    #  Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.        #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
    #
    #  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
    #  Time Complexity of Solution:
    #  Best = Average = Worst = O(nlog(n)).
    #  Approach:
    #   Merge sort is a divide and conquer algorithm. In the divide and
    #   conquer paradigm, a problem is broken into pieces where each piece
    #   still retains all the properties of the larger problem -- except
    #   its size. To solve the original problem, each piece is solved
    #   individually; then the pieces are merged back together.
    #
    # step 1 -divide list using  mid = len(aList) // 2
    # step 2 -take left part for sorting [left = merge sort(aList[:mid])]
    # step 3 -take right part for sorting  [right= merge sort(aList[mid:])]
    #         sort until only one element is present in the list
    # step 4 - Again the sorted element is merge back using same reverse process

    # Implementation of Merge sort

    def mergeSort(self, smaplelist):
        print("Splitting ", smaplelist)
        if len(smaplelist) > 1: # divide list until one element is present in list
            mid = len(smaplelist) // 2
            lefthalf = smaplelist[:mid]
            righthalf = smaplelist[mid:]

            self.mergeSort(lefthalf)  # calling merge sort function on left part of list
            self.mergeSort(righthalf) # calling merge sort function on right part of list

            leftindex = 0
            rightindex = 0
            newlistindex = 0

            while leftindex < len(lefthalf) and rightindex < len(righthalf):
                if lefthalf[leftindex] < righthalf[rightindex]:   # comparing the elements
                    smaplelist[newlistindex] = lefthalf[leftindex]  # copying the element in new list
                    leftindex= leftindex + 1
                else:
                    smaplelist[newlistindex] = righthalf[rightindex]
                    rightindex = rightindex + 1
                    newlistindex = newlistindex + 1

            while leftindex < len(lefthalf):
                smaplelist[newlistindex] = lefthalf[leftindex]
                leftindex = leftindex + 1
                newlistindex = newlistindex + 1

            while rightindex < len(righthalf):
                smaplelist[newlistindex] = righthalf[rightindex]
                rightindex = rightindex + 1
                newlistindex = newlistindex + 1
        print(" List is sorted successfully using Merge sort ", smaplelist)

    # =======================================*****==================================================

    # Quick Sort

    #  Statement: Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2]
    #
    #  Sample Output: [0,1,2,3,4,5,6,7,8,9]
    #
    #  Time Complexity of Solution:
    #  Best = Average = O(nlog(n)); Worst = O(n^2).
    #
    #  Approach:
    #  In Quick sort we first select any pivot then divide the value less than the pivot at left side of array
    #  and values greater than on the right side of the array
    #  we apply this recursively until the list not get sorted

    # step 1 - Pick a “pivot” element.
    # step 2 - “Partition” the array into 3 parts:
    # step 3 - left part: all elements in this part is less than the pivot.
    # step 4 - Second part: the pivot itself (only one element!)
    # step 5 - Third part: all elements in this part is greater than or equal to the pivot.
    # step 6 - Then, apply the quick sort algorithm to the first and the third part. (recursively)

    # Method implementation for Quick Sort

    def quickSort(self, samplelist):
        self.quickSortHelper(samplelist, 0, len(samplelist) - 1)

    def quickSortHelper(self, samplelist, first, last):
        if first < last:
            splitpoint = self.partition(samplelist, first, last)

            self.quickSortHelper(samplelist, first, splitpoint - 1)
            self.quickSortHelper(samplelist, splitpoint + 1, last)

    def partition(self, samplelist, first, last):
        pivotvalue = samplelist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and samplelist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while samplelist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = samplelist[leftmark]
                samplelist[leftmark] = samplelist[rightmark]
                samplelist[rightmark] = temp

        temp = samplelist[first]
        samplelist[first] = samplelist[rightmark]
        samplelist[rightmark] = temp

        return rightmark
    #=======================================*****==================================================

    #@@ Radix Sort

    #  Statement: Given a disordered list of integers (or any other items),
    #  rearrange the integers in natural order.
    #
    #  Sample Input: [8,5,3,1,9,6,0,7,4,2]
    #
    #  Sample Output: [0,1,2,3,4,5,6,7,8,9]
    #
    #  Time Complexity of Solution:
    #  Best = Average = O(nlog(n));
    # Worst case = O(nk)

    #  Approach:
    # In Radix sort we check digits places like unit,ten, hundred and so on
    # depending on this value we sorted the digits in different buckets i.e. 0 to 9
    # same logic apply for all digits
    # and this sorted again append back to the list according to the digits

    # step 1 - Take sample list and create the 10 buckets as lists having 0 to 9
    # step 2 - sort the number according to the unit place digit in buckets then copy again to list
    # step 3 - Again by using tens place again append to list
    # step 4 - steps are repeated again and again until the list no get sorted

    #  Method for the Radix Sort

    def radix_sort(self, samplelist, base=10):
        def list_to_buckets( samplelist, base, iteration):
            buckets = [[] for x in range(base)]
            for number in samplelist:
                # Isolate the base-digit from the number

                digit = (number // (base ** iteration)) % base
                # Drop the number into the correct bucket
                buckets[digit].append(number)
            return buckets

        def buckets_to_list(buckets):
            numbers = []
            for bucket in buckets:
                # append the numbers in a bucket
                # sequentially to the returned array
                for number in bucket:
                    numbers.append(number)
            return numbers

        maxval = max(samplelist)

        it = 0
        # Iterate, sorting the array by each base-digit
        while base ** it <= maxval:
            samplelist = buckets_to_list(list_to_buckets(samplelist, base, it))
            it += 1

        return samplelist
        print(samplelist)
    # =======================================*****==================================================


# Implementation for the user input
# Options provided to the user


while True:
    print("1.Bubble Sort\n"
          "2.Selection Sort\n"
          "3.Insertion Sort\n"
          "4.Merge sort\n"
          "5.Quick Sort\n"
          "6.Radix Sort\n"
          "7.Exit the Process ")

    menu = int(input(print("*******Select the sorting option You want to sort*******\n")))

    # if press 1 then user will get the bubble sort output

    if menu == 1:
        sample = [int(x) for x in input("=>Please enter the values with spaces you want to Bubble Sort   :").split()]
        s1 = Sorting(sample)  # creating object of class
        s1.BubbleSort(sample)  # calling bubble Sort method

    elif menu == 2:
        sample = [int(x) for x in input(" =>Please enter the values with spaces you want to Selection Sort :  ").split()]
        s2 = Sorting(sample)
        s2.selectionSort(sample)  # calling Selection sort method

    elif menu == 3:
        sample = [int(x) for x in input("=>Please enter the values with spaces you want to Insertion Sort :").split()]
        s3 = Sorting(sample)
        s3.insertionSort(sample)  # Calling insertion sort method

    elif menu == 4:
        sample = [int(x) for x in input("=>Please enter the values with spaces you want to Merge Sort :").split()]
        s4 = Sorting(sample)
        s4.mergeSort(sample)  # Calling Merge sort method

    elif menu == 5:
        sample = [int(x) for x in input("=>Please enter the values with spaces you want to Sort :").split()]
        s5 = Sorting(sample)
        s5.quickSort(sample)  # Calling Quick sort method

    elif menu == 6:
        sample = [int(x) for x in input("=>Please enter the values you want to Radix Sort : ").split()]
        s6 = Sorting(sample)
        s6.radixsort(sample)  # Calling insertion sort method

    elif menu == 7:
        exit(print('Exited successfully'))  # user will exit the process successfully

    elif menu == 8 or 9 or 0:

        print("Invalid Menu selected")


