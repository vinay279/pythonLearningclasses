from random import choice, randint
from string import  *
from StudentDataSorting.SortNameAgeScore import SortNameAgeScore as s


class TestStudentDataSorting:
        studentData = []


        def takeStudentData(self):
            NumberOfStudent = int(input("Enter Number of Student ="))
            for rowsInMatrix in range(0, self.NumberOfStudent):
                self.studentData.append([])

            for row in range(0, self.NumberOfStudent):
                name = ''.join(choice(ascii_lowercase) for i in range(3))
                Age = randint(1, 99)
                Score = randint(22, 99)
                tpl = [name, Age, Score]
                self.studentData[row] = tpl
            print('Unsorted List Of Students', self.studentData)
            return self.studentData

        def AutomatedSort(self, sortIndex):
            data = self.studentData
            length = len(data)
            for outer in range(0, length):  # for tracing the list from start to end
                for inner in range(0, length - 1 - outer):  # it will skip the last element which is already sorted
                    # Sorting Student data by Name
                    if sortIndex == 0:
                        firstElement = data[inner][sortIndex]
                        secondElement = data[inner + 1][sortIndex]
                        s.swap(firstElement, secondElement, inner)

                    elif sortIndex == 1 or 2:
                        firstElement = int(data[inner][sortIndex])
                        secondElement = int(data[inner + 1][sortIndex])
                        s.swap(firstElement, secondElement, inner)
                        # if age and score are equal then sort according to name first
                        if firstElement == secondElement:
                            s.swap(firstElement, secondElement, inner)


                print('Sorted List Of Students', data)


c = TestStudentDataSorting()
c.takeStudentData()