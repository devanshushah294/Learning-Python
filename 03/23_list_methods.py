list_a = [6, 7, 8, 3, 3, 3]
# To add the element at the last of the list we need to use the append method
print(list_a)
list_a.append(25)
print(list_a)

# To add the element at the specific index of the list we need to use the append method
# list_a.insert(element, index)
list_a.insert(29, 0)
print(list_a)

# To sort the array we use sort method
list_a.sort()
print(list_a)
list_a.reverse()
print(list_a)

# index method returns the first occurrence of the element in the list
print("number 3 is at", list_a.index(3), "index")

# To find the count of number of occurence in the list we use count method
print("3 comes", list_a.count(3), "times in the list")

list_b = [23, 45, 67, 45]
list_c = list_b
list_c[0] = 34
print(list_b)  # will give the output [34, 45, 67, 45]

# For not changing the original list we need to make the copy
list_b = [23, 45, 67, 45]
list_c = list_b.copy()
list_c[0] = 34
print(list_b)  # will give the output [34, 45, 67, 45]

# To add the elements of one list to another we use extend method
list_b.extend(list_c)
print(list_b)

# one more method is there to make a new list that will add both list
list_d = list_b + list_c
print(list_d)
