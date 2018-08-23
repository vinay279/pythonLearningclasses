class Student_1:
    '''this class is for the demo'''

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def info(self):
        print('name of student ',self.name)
        print('rollno of student',self.rollno)

s1=Student_1('vinay',222)
s1.info()
print(Student_1.__doc__)
s2= Student_1("vinay",1222)
s2.info()