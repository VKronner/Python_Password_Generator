import department as dp
import password


class myUser:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.__myDepartment = ''
        self.__email = ''
        self.__password = ''

        myUser.setEmail(self)
        myUser.setPassword(self)
        myUser.setDepartment(self)
        myUser.setEmail(self)

    def setDepartment(self):
        while True:
            departmentChoice = input("Enter the option for the department.\n\n"
                                   "1 - HR\n"
                                   "2 - IT\n"
                                   "3 - Marketing\n"
                                   "4 - Sales\n"
                                   "5 - Other\n"
                                   "Chose one of the Above Options..::: ")
            match departmentChoice:
                case '1':
                    self.__myDepartment = dp.myDepartment("HR")
                    break
                case '2':
                    self.__myDepartment = dp.myDepartment("IT")
                    break
                case '3':
                    self.__myDepartment = dp.myDepartment("Marketing")
                    break
                case '4':
                    self.__myDepartment = dp.myDepartment("Sales")
                    break
                case '5':
                    self.__myDepartment = dp.myDepartment("Other")
                    break
                case _:
                    print("Please choose one of the options given.\n\n"
                          "1 - HR\n"
                          "2 - IT\n"
                          "3 - Marketing\n"
                          "4 - Sales\n"
                          "5 - Other\n"
                          "Chose one of the Above Options..::: ")


    def getPassword(self):
        if self.__password == '':
            myPass = password.myPassword
            self.__password = myPass.setFirstPassword(self)
        return self.__password
    def getDpName(self):
        return self.__myDepartment.getName()
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def getEmail(self):
         return self.__email

    def setEmail(self):
        self.__email = '{}.{}@CompanyName.com.ca'.format(self.first, self.last).lower()

    def setPassword(self):
        myPass = password.myPassword
        self.__password = myPass.setFirstPassword(self)
        return self.__password