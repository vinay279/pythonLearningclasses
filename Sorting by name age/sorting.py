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
    while True:


        infos = int(input("how many student data you want to enter "))
        print("Enter The Student Information")
        infoList = []
        for info in range(0, infos):
            infoList.append([])

        for row in range(0, infos):
            for col in range(0,3):
                infoList[row].append(col)

                if col == 0:
                    infoList[row][col] = input("Enter Name of student").format

                if col == 1:
                    infoList[row][col] = int(input("Enter Age student").format())
                if col == 2:
                    infoList[row][col] = int(input("Enter Score"))
                print('\n')

        for name in range(0, infos):
            infoList[row][name]
        print(infoList)








