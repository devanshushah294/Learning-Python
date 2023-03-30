# lists are the ordered collection of data items.
# They stores multiple items in a same variable.
# list items are seperated by comma and enclosed in a square brackets.
# They are changable meaning we can alter them after creation - means they are mutable

list_a = [3, 6, 5, "Devanshu", True, ["Devanshu", 23, 4],]
print(type(list_a))
print(list_a)
print(list_a[0])
print(list_a[-1])

# It gives IndexError if the index given in square brackets are out of bound.
# Just like array index out of bound error in java.
# ex print(list_a[10])

# also you can interate over the list very easily in python
for i in list_a:
    print(i)

# also we can check the availability of the item in list using in keyword
# also valid for string
if (6 in list_a):
    print("Yes")
else:
    print("No")

# print(list_a) will print the complete list in python
print(list_a)
# To print the list from the specific index we need to do
print(list_a[2::])  # will print the complete list from the index 2
print(list_a[:3:])  # will print the list from starting to index 3
# will print the list items from index 0 and skiping 1 indexes
print(list_a[::2])
# will print the list items from index 1 and skiping 1 indexes
print(list_a[1::2])
# will print the list items from index 0 and skiping 2 indexes
print(list_a[::3])
# list comprehension is an easy way to generate list for a given pattern
list_b = [i for i in range(1, 10)]
print(list_b)
# will give list like [1,2,3,4,5,6,7,8,9]

list_c = [i*i for i in range(1, 10)]
print(list_c)
# will give list like[1,4,9,16,25,36,49,64,81]
