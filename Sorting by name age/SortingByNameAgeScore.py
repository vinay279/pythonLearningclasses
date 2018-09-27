'''You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]'''

class SortNameAgeScore:
    studentData = []

    def takeStudentData(self):
        NumberOfStudent = int(input("Enter Number of Student ="))

        for rowsInMatrix in range(0, NumberOfStudent):
            self.studentData.append([])

        for row in range(0, NumberOfStudent):
            Data = input('Enter student Data like(EX - tom,19,80 ) = ')  # 'Tom,19,80'
            Data.casefold()
            tpl = tuple(Data.split(','))
            self.studentData[row] = tpl

        print('Unsorted List Of Students', self.studentData)
        return self.studentData

    def Sort(self, sortIndex):

        length = len(self.studentData)
        for outer in range(0, length):  # for tracing the list from start to end
            for inner in range(0, length - 1 - outer):  # it will skip the last element which is already sorted

                if sortIndex == 0:
                    firstElement = str(self.studentData[inner][sortIndex])
                    secondElement = str(self.studentData[inner+1][sortIndex])
                    firstElement.casefold()
                    secondElement.casefold()

                    if firstElement > secondElement:  # comparing two elements
                        self.studentData[inner], self.studentData[inner + 1] = self.studentData[inner + 1], self.studentData[inner]  # swapping two element

                elif sortIndex == 1 or 2:
                    firstElement = int(self.studentData[inner][sortIndex])
                    secondElement = int(self.studentData[inner + 1][sortIndex])

                    if firstElement > secondElement:  # comparing two elements
                        self.studentData[inner], self.studentData[inner + 1] = self.studentData[inner + 1], self.studentData[inner]

                    elif firstElement == secondElement:
                        firstElement = str(self.studentData[inner][0])
                        secondElement = str(self.studentData[inner + 1][0])
                        firstElement.lower()
                        secondElement.lower()

                        if firstElement > secondElement:  # comparing two elements
                            self.studentData[inner], self.studentData[inner + 1] = self.studentData[inner + 1],self.studentData[inner]


        print('Sorted List Of Students', self.studentData)

    def callSort(self):
        while True:
            print(' The sorting Gives priority to capital Alphabet first And then small Letters')
            print('Select From The Options Of Sorting')
            print("1.Sort by Name\n"
                  "2.Sort By Age\n"
                  "3.Sort By Score\n"
                  "4.exit")
            sortIndex = int(input("Enter Number"))
            if sortIndex == 1:
                self.Sort(0)
                print('Sorted List Of Students By Using Name\n')
            elif sortIndex == 2:
                self.Sort(1)
                print('Sorted List Of Students By Using Age\n')
            elif sortIndex == 3:
                self.Sort(2)
                print('Sorted List Of Students By Using Score\n')
            elif sortIndex == 4:
                break

f = SortNameAgeScore()
f.takeStudentData()
f.callSort()
