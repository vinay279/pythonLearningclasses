class Insertion:
    # =======================================*****==================================================

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
        return samplelist
    # =======================================*****==================================================
