class QuickS:
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
        print('Quick sort list is = ', samplelist)

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

