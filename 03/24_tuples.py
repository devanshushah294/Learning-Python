# Tuple is a immutable data structure in python it can't be changed once it is made
# at the time of makeing the tuple you need to provide the values
tup = (1, 2, 6)
print(type(tup))
print(tup)
print(tup[0])
print(tup[2])
print(tup[1])
# print(tup[3]) will give an error as length is 3

# For single element in round bracketes python takes it as int
tup2 = (3)
print(type(tup2))

# also like other data structure we can check the presence/absence of the elements in tuple
# using membership operators like -- in and not in

if (2 in tup):
    print("yes 2 is present")
else:
    print("2 is not present")
if (3 not in tup):
    print("No 3 is not present")
else:
    print("yes 3 is present")

# also slicing can be done in tuples
# example
# slicing in python will never give an IndexError (or index out of bound error)
# if the index will be out of bound then it will return and empty iterable and to prevent user from error
# ex
tup2 = tup[0:40:1]
print(tup2)  # will give (1,2,6)
# string are immutable
# tuples are immutable
# lists are mutable
