class Radix:
    #  Radix Sort

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

    # Python program for implementation of Radix Sort

    # A function to do counting sort of arr[] according to
    # the digit represented by exp.
    # counting
    # Method for Radix sort
    def radixSort(self, arr):

        # Find the maximum number to know number of digits
        max1 = max(arr)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 0:
            self.digitcounting(arr, exp)
            exp *= 10

        print(" This is the radix sorted list ", arr)

    def digitcounting(self, arr, exp1):

        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (arr[i] // exp1)
            count[(int(index) % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp1)
            output[count[(index) % 10] - 1] = arr[i]
            count[(index) % 10] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

