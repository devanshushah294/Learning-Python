# python don't support do while loops
# to use it we do like this:
a = 0
while (True):
    # code
    print(a)
    a += 1
    if (a % 100 == 0):
        break
