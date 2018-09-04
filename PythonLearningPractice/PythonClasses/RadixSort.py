def radixsort(self,samplelist):
    "sort list of integers using base-10 radix sort"

    if samplelist:
        buckets = [ [],[],[],[],[],[],[],[],[],[] ]

        # get largest element to determine when sort is done
        maxval = max(samplelist)
        # decimal digit currently partitioning on (1,10,100...)
        digit = 1

        while maxval > digit:
            # append each element of a to the end of the bin
            # corresponding to the partition digit
            for values in samplelist:
                buckets[(values/digit) % 10].append(values)

                digit = digit * 10

            # move values from bins back to a single list
            samplelist = []
            for index in range(10):
                samplelist.extend(buckets[index])
                buckets[index] = []

    return samplelist