# when we want to skip the perticular iteration in python we use continue statement
# when we want to break the loop after the perticular iteration we use break statement
a = 0
while (True):
    # code
    a += 1
    if (a % 10 == 0 and a % 100 != 0):
        continue
    print(a)
    if (a % 100 == 0):
        break
