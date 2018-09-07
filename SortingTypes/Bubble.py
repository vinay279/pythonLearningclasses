class BubbleSort:


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
    pass


