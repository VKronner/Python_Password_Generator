import user

if __name__ == '__main__':
    print("Register of New Employ.")
    firstName = input("Enter First Name..::: ")
    lastName = input("Enter Last  Name..::: ")

    user1 = user.myUser(firstName,lastName)

    print("\n\nWorker -> " + user1.fullname())
    print("Email -> " + user1.getEmail())
    print("Department -> " + user1.getDpName())
    print("Password -> " + user1.getPassword())