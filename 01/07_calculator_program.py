a = int(input('Enter the number1 : '))
b = int(input('Enter the number2 : '))
c = input('enter operator : ')
if (c == '+'):
    answer = a + b
elif (c == '-'):
    answer = a - b
elif (c == '*'):
    answer = a * b
elif (c == '/'):
    answer = a / b
elif (c == '^'):
    answer = a ** b
elif (c == 'rem'):
    answer = a % b
elif (c == 'quotient'):
    answer = a // b
else:
    print("Enter correct input : ")
print(answer)
