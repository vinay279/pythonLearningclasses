from Tools.demo.sortvisu import quicksort


class Quicksort():
    def __init__(self,array, start, end):
        self.ar = array
        self.quick_sort(array,start, end)

    def quick_sort(self, array, start, end):
        if start < end:
            pivot = self.partition(array,start,end)
            self.quick_sort(array,start,pivot-1)
            self.quick_sort(array,pivot+1,end)

    def partition(self,array,start,end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):

             if array[j] <= x:
                 i += 1
                 if i<j:
                     z = array[i]
                     array[i] = array[j]
                     array[j] = z
        return i
c=Quicksort()
c.quick_sort()