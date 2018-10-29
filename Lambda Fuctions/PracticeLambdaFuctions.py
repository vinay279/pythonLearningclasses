from functools import reduce
class PracticePython:
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def find_square(self):
        """
        1)Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]
        :return:
        """

        root_list = list(map(lambda x: x**2,self.list1))
        print('list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10] ===',root_list)

    def find_square_of_even(self):
        """
        Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10
        :return:
        """
        square_of_even = list(map(lambda x: x ** 2,list(filter(lambda x: x % 2 == 0,self.list1))))
        print('even numbers',square_of_even)


    def find_factorial(self):
        """
        3) Finding Factorial of given number
        :return:
        """
        number = int(input("enter number to find factorial"))
        Factorial = list(reduce(lambda x,y: x*y,range(1,number+1)))
        print(Factorial)



ObjClass = PracticePython()
ObjClass.find_square()
ObjClass.find_square_of_even()
ObjClass.find_factorial()