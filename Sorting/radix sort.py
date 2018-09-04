def radix_sort(array, base=10):
    def list_to_buckets(array, base):
        buckets = [[] for x in range(base)]
        for number in array:
            # Isolate the base-digit from the number
            digit = (number // base ) % base
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

    maxval = max(array)

    it = 0
    # Iterate, sorting the array by each base-digit
    while base ** it <= maxval:
        array = buckets_to_list(list_to_buckets(array, base, it))
        it += 1

    return array

sample = [int(x) for x in input().split()]
radix_sort(sample)