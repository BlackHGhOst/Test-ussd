
#HealthCentre
def HC():
    Hospital = input("Registered Health Centre: ")
    if len(Hospital) < 30 and Hospital.isalpha():
        print("Thank You\n"
              "Information Saved\n"
              "Successfully\n"
        )
    else:
        print("Invalid Response\n"
              "Try Again\n"
        )
        HC()

#Number of Children
def NoC():
    Number_Of_Children = input("Enter Number of Children: ")
    if len(Number_Of_Children) < 11 and Number_Of_Children.isnumeric():
        HC()
    else:
        print("Invalid Number\n"
              "Try Again\n"
        )
        NoC()


#Nrc Entry
def NRCnumber():
    nrc = input("Enter NRC Number: ")
    if len(nrc) == 9 and nrc.isnumeric():
        NoC()
    else:
        print("Invalid NRC\n"
              "Try Again\n"
        )
        NRCnumber()

#Registration
def Register():
    name = input("Please Enter Name: ")
    if len(name) <= 20 and name.isalpha():
        NRCnumber()
    else:
        print(
            "Invalid Name\n"
            "Try Again\n"
        )
        Register()


# Menu Options
def Menu():
    MenuCode = input(
        "1. Register\n"
        "2. About Us\n"
        "3. Help\n"
    )
    if MenuCode == "1":
        Register()
    elif MenuCode == "2":
        print("We are blah blah\n"
              "and here to help blah\n")
    elif MenuCode == "3":
        print("Enter 1 for full registration\n"
              "Enter 2 for a brief discussion about us\n")
    else:
        print("Invalid USSD code\n"
              "Try Again"
        )
        USSDcheck()


# Cross-Checking Function
def USSDcheck():
    ussd = input("Enter USSD code: ")
    if ussd == "*1234#":
        Menu()
    else:
        print("invalid USSD code\n"
              "Try Again"
        )
        USSDcheck()

# Calling the USSD function
USSDcheck()