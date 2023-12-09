import random
print("Enter 0 for stone")
print("Enter 1 for paper")
print("Enter 2 for sizzor")
computer_score = 0
user_score = 0
while (computer_score < 5 and user_score < 5):
    print("Enter your input : ")
    user_input = int(input("Enter the number"))
    computer_input = random.randint(0, 2)
    print(computer_input)
    if (user_input == 0):
        if (computer_input == 0):
            pass
        elif (computer_input == 1):
            computer_score += 1
        elif (computer_input == 2):
            user_score += 1
    elif (user_input == 1):
        if (computer_input == 1):
            pass
        elif (computer_input == 0):
            user_score += 1
        elif (computer_input == 0):
            computer_score += 1
    elif (user_input == 2):
        if (computer_input == 2):
            pass
        elif (computer_input == 1):
            user_score += 1
        elif (computer_input == 0):
            computer_score += 1
    else:
        print("Enter correct input")
    print("user score = ", user_score)
    print("conputer score = ", computer_score)
if (user_score > computer_score):
    print("user wins")
else:
    print("computer wins")
