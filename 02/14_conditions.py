age = int(input("Enter your age"))
# here the space repressents the indendation which is must important in python represents a block
if (age > 18):
    print("You can drive")
else:
    print("You can't drive")
# if we want to keep the block empty in python there is a pass keyword
number = int(input("Enter the number : "))
if (number < 0):
    print("Number is negative")
elif (number == 0):
    print("Number is zero")
elif (number == 999):
    print("number is special")
elif (number > 0):
    print("Number is positive")
print("I am Satisfied now")
