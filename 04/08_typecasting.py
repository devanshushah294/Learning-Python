# confusing output 1+2 = 12 by below given code as they are not converted to integer treated as string and then concatenated
a = input("Enter the number 1 ")
b = input("Enter the number 2 ")
print(a+b)

# thus type casting comes into picture
# two types of type casting

# 1) implicit and 2) explicit

# 1) Explicit
a = int(a)
b = int(b)
print(a+b)

# 2) Implicit
a = 2.3
b = 3
# python automatically converts the smaller datatype to higher level datatype with which it performs operations
print(a+b)
