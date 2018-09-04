class SelectionSort:
    # constructer with the sample list
    def __init__(self,samplelist):
        self.samplelist = samplelist

    #method used for the selection sort purpose

    def selectionsort(self):
        for index in range(len(self.samplelist)):
            minindex = index
            j= index+1
            while (j < len(sample)):
                if (sample[j] < sample[minindex]):
                    minindex = j
                    j+= 1
                    sample[i], sample[minindex] = sample[minindex], sample[i]


        print('sorted values are : ',sample)
sample =[int(x) for x in input("please enter the numbers ").split()]
a= SelectionSort(sample)
a.selectionsort(sample)