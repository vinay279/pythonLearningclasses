
class MergeSort:
    ''' This class is for Merge Sort'''

    def mergesort(self,A):
        self.mergesort_2(A, 0, len(A)-1)

    def mergesort2(self,A, first, last):
        if first < last:
            middle = (first+last)//2
            self.mergesort2(A, first, middle)
            self.mergesort2(A, middle+1, last)
            self.merge(A, first, middle, last)

    def merge(A, first, middle, last):
        L = A[first:middle]
        R = A[middle:last+1]
        L.append(999999999999)
        R.append(999999999999)
        i = j = 0
        for k in range(first, last+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

