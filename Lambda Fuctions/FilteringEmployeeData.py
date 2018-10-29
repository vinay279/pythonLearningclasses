class GetEmpData:
    emp_data = [{'name': "emp_1", 'salary': 10000, 'experience': 1},
                {'name': "emp_2", 'salary': 20000, 'experience': 2},
                {'name': "emp_3", 'salary': 30000, 'experience': 3},
                {'name': "emp_4", 'salary': 40000, 'experience': 4},
                {'name': "emp_5", 'salary': 55000, 'experience': 5},
                {'name': "emp_6", 'salary': 60080, 'experience': 6},
                {'name': "emp_7", 'salary': 70000, 'experience': 6},
                {'name': "emp_8", 'salary': 80800, 'experience': 7},
                {'name': "emp_9", 'salary': 90100, 'experience': 8},
                {'name': "emp_10", 'salary': 150000, 'experience':11},


    ]

    salary = int(input("Enter salary"))


    def find_sal_less_than(self,salary):
        salary = int(input("Enter salary"))
        sal = list(filter(lambda x: x["salary"] < salary,self.emp_data))
        print(sal)

    def find_sal_greater_than(self,salary):
        salary = int(input("Enter salary"))
        sal = list(filter(lambda x: x["salary"] > salary, self.emp_data))
        print(sal)

    def find_exp_greater_than(self,experience):
        experience = int(input("Enter experience"))
        exp = list(filter(lambda x: x["experience"] > experience, self.emp_data))
        print(exp)

    def find_exp_less_than(self,experience):
        experience = int(input("Enter experience"))
        exp = list(filter(lambda x: x["experience"] < experience, self.emp_data))
        print(exp)




