
class QuickSort:

    '''this class is used for the Quick Sort'''
    def __init__(self, samplelist,start,end):
        self.samplelist = samplelist
        self.start = start
        self.end = end

    def partition(self):
        length = len(self.samplelist)
        index = self.start
        current = self.start
        pivot = self.samplelist[self.end]
        while current < length:
            if self.samplelist[current] <= pivot:
                self.samplelist[index], self.samplelist[current] = self.samplelist[current], self.samplelist[index]
                index += 1
                current += 1
                self.samplelist[index], self.samplelist[self.end] = self.samplelist[self.end], self.samplelist[index]
                print('After partition')
                return index

    # this method is use for the quick sorting##
    def quicksort(self):
        if self.start < self.end:
            index = self.partition(self.samplelist, self.start, self.end)  # middle part
            self.quicksort(self.samplelist, self.start, index - 1)  # left side recursion
            self.quicksort(self.samplelist, index + 1, self.end)  # right side recursion
            print('this is quicksort output', self.samplelist)


sampl =[int(x) for x in input("please enter the numbers to sort using QuickSort : ").split()]
a= QuickSort(sampl,int(0),int(3))
a.quicksort(sampl, int(0), len(sampl)-1)