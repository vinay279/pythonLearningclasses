class Merge:
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
    # step 2 -take leftpart for sorting [left = mergesort(aList[:mid])]
    # step 3 -take rightpart for sorting  [right= mergesort(aList[mid:])]
    #         sort until only one element is present in the list
    # step 4 - Again the sorted element is merge back using same reverse process

    # Implementation of Merge sort

    # function for merging two sub-arrays
    def merge(self, left, right, Array):
        i = 0
        j = 0
        k = 0

        while (i < len(left) and j < len(right)):
            if (left[i] < right[j]):
                Array[k] = left[i]
                i = i + 1
            else:
                Array[k] = right[j]
                j = j + 1

            k = k + 1

        while (i < len(left)):
            Array[k] = left[i]
            i = i + 1
            k = k + 1

        while (j < len(right)):
            Array[k] = right[j]
            j = j + 1
            k = k + 1
            return Array

    # function for dividing and calling merge function
    def mergesort(self, Array):
        n = len(Array)
        if (n < 2):
            return

        mid = n // 2
        left = []
        right = []

        for i in range(mid):
            number = Array[i]
            left.append(number)

        for i in range(mid, n):
            number = Array[i]
            right.append(number)

        a= self.mergesort(left).extend(self.mergesort(right))
        # calling merge
        self.merge(left, right, Array)
        print(Array)





