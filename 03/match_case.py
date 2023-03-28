# basic example
a = int(input("Enter the number : "))
match a:
    case 0:
        print("Number is Zero")
    case 4:
        print("Number is 4")
    case _ if (a != 20):
        print("Number is not 20")
    case _ if (a != 30):
        print("Number is not 30")

# For default use underscore in python
# python automatically gives break after the case is matched
