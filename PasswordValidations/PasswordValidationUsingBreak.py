'''A website requires the users to input username and password to register.
 Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and
ill check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.'''
class CheckPasswordValidationUsingBreak:
    def checkUpperChar(self, input):
        uppers = 0
        upper_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
        for char in input:
            if char in upper_list:
                print("only One comparision takes place after that loop break", char)
                uppers += 1
                break
        if uppers > 0:
            return True
        else:
            return False

    def checkLowerChar(self, input):
        lowers = 0
        lower_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
        for char in input:
            if char in lower_list:
                lowers += 1
                break
        if lowers > 0:
            return True
        else:
            return False

    def checkDigit(self, input):
        numbers = 0
        number_list = "1 2 3 4 5 6 7 8 9 0".split()
        for char in input:
            if char in number_list:
                numbers += 1
                break
        if numbers > 0:
            return True
        else:
            return False

    def checkspecialchar(self,input):
        specials = 0
        special_list = " @ $ # ".split()
        for char in input:
            if char in special_list:
                specials += 1
        if specials > 0:
            return True
        else:
            return False

    def checkLength(self, input):
        if 6 <= len(input) <= 12:
            return True
        else:
            return False

    def checkValidPassword(self):

        inputPassword = input("Enter Password Separated by comma\n"
                              "**Password should contains \n"
                              "At least one Lower Alphabet\n"
                              "At least one Upper Alphabet\n"
                              "At least one digit from (0to9)\n"
                              "At least one special char (# or @ or $)")
        passwordlist = inputPassword.split(",")
        validPasswords = []
        for password in passwordlist:
            if (self.checkUpperChar(password) and self.checkLowerChar(password) and self.checkDigit(password) and
                self.checkspecialchar(password) and self.checkLength(password)) is True:
                validPasswords.append(password)
        print(validPasswords)

d = CheckPasswordValidationUsingBreak()
d.checkValidPassword()