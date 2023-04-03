# here a = 9 will give default value to the argument a
# similarly b = 3 will give default value to argument to b when nothing will be assigned to a or b
# then its default value will be accessed
def average(a=9, b=3):
    print("avg = ", (a + b)/2)


average(2, 4)  # will give 3
average()  # will give 6
average(3)  # will give 3

# keyword arguments
# In case if we don't pass the arguments in the key = value syntax
# we need to follow the order but if we use such syntax then we need not need to worry about it
# example above function can be called like
average(a=20, b=30)

# Required arguments
# at the time of defining the function if we don't give the default value to any argument
# then it will be automatically be required argument
# example


def welcome(name, surname):
    print("Hello,", name, surname)


welcome("Devanshu", "Shah")
# or
welcome(name="Devanshu", surname="Shah")
# if we don't pass the arguments then it will give an error like welcome("Mubin")


# If we want to give variable length arguments then

# Arbitary arguments
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("average is", sum/len(numbers))


average(2, 3, 4, 56, 7, 7)

# Keyword Arbitrary Arguments:


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")

# return statement


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum/len(numbers)


print(average(2, 3, 4, 5, 6))

# Also we can return multiple values and if and during the time of calling we can get values in form of tuple whic we can do unpacking


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum/len(numbers), 2


a = average(2, 3, 4, 5, 6)
print(type(a))
