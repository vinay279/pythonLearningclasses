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
    will check them according to the above criteria. Passwords that match the criteria are to be printed,
    each separated by a comma.'''

class PasswordValidationUsingAscii:
    def checkupperChar(self, input):
        uppers = 0
        for char in input:
            letter = ord(char)
            if 65 <= letter <= 90:
                uppers += 1
                break
        if uppers > 0:
            return True
        else:
            return False

    def checkLowerChar(self, input):
        lower = 0
        for char in input:
            letter = ord(char)
            if 97 <= letter <= 122:
                lower += 1
                break
        if lower > 0:
            return True
        else:
            return False

    def checkDigit(self, input):
        numbers = 0
        digits = "1 2 3 4 5 6 7 8 9 0".split()
        for char in input:
            if char in digits:
                numbers += 1
                break
        if numbers > 0:
            return True
        else:
            return False

    def checkspecialchar(self, input):
        specialChars = 0
        specialCharList = " @ $ # ".split()
        for char in input:
            if char in specialCharList:
                specialChars += 1
                break
        if specialChars > 0:
            return True
        else:
            return False

    def checkLength(self, input):
        if 6 <= len(input) <= 12:
            return True
        else:
            return False

    def checkValidPassword(self):
        while True:
            inputPassword = input("Enter Password Separated by comma\n"
                                  "**Password should contains \n"
                                  "At least one Lower Alphabet\n"
                                  "At least one Upper Alphabet\n"
                                  "At least one digit from (0to9)\n"
                                  "At least one special char (# or @ or $)")
            passwordList = inputPassword.split(",")
            validPasswords = []
            for password in passwordList:
                if (self.checkupperChar(password) and self.checkLowerChar(password) and self.checkDigit(password) and
                    self.checkspecialchar(password) and self.checkLength(password)) is True:
                    validPasswords.append(password)
            print("The valid Password From the List You Entered =", validPasswords)

d = PasswordValidationUsingAscii()
d.checkValidPassword()

