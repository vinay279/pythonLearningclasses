class Selection:
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
        global positionOfMax
        for fillslot in range(len(samplelist) - 1, 0, -1):
            positionOfMax = 0
            for location in range(1, fillslot + 1):
                if samplelist[location] > samplelist[positionOfMax]:
                    positionOfMax = location

            temp = samplelist[fillslot]
            samplelist[fillslot] = samplelist[positionOfMax]
            samplelist[positionOfMax] = temp

        print('sorted values are : ', samplelist)
        return positionOfMax

