import passwordConstants as const
import random

class myPassword:
    def __init__(self):
        self.__password = []
        self.__passwordLength = const.DEFAULT_PASSWORD_LIMIT_LENGTH

    def getPassword(self):
        return self.__password

    def setFirstPassword(self):

        passwordGenerator = const.DEFAULT_PASSWORD_GENERATOR
        __password = ""
        for i in range(const.DEFAULT_PASSWORD_LIMIT_LENGTH):
            random_index = random.randint(0, len(passwordGenerator) - 1)
            __password += passwordGenerator[random_index]

        return __password
    def setPassword(self, myPassword):

         self.__password = myPassword