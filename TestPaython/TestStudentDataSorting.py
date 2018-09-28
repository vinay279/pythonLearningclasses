from random import choice, randint
from string import  *
from StudentDataSorting.SortNameAgeScore import SortNameAgeScore as s


class TestStudentDataSorting:
        studentData = []
        tuples = int(input("Enter How Many Tuples You Want"))
        def genrate(self):
            name = ''.join(choice(ascii_lowercase) for i in range(3))
            Age = randint(1, 99)
            Score = randint(22, 99)
            tpl = (name, Age, Score)
            return tpl

        for rowsInMatrix in range(0, tuples):
            studentData.append([])
        for row in range(0, tuples):

            studentData[row] = tpl
        print(studentData)

