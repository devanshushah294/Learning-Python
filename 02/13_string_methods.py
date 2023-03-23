# strings are immutable in python
a = "Mubin"
print(a)

# here a is not changed but a new address is given to reference a
a = "Devanshu"
print(a)

a.upper()  # here string a is not changed because strings are immutable
print(a)

# but we can change them by this way by giving the reference an new address
a = a.upper()
print(a)
print(a.lower())
print(a.capitalize())

str = "Darshan Institute"
print(str)
str = str.replace("Institute", "University")
print(str)

csv = "Kenil,Heet,Mubin,Divyank,Diya,Krishita"
list = csv.split(",")
print(list)
blogHeading = "introDUCtion tO js"
print(blogHeading.capitalize())
welcomeString = "Welcome to Console !!!"
print(welcomeString.center(50))
print(welcomeString.endswith("!!!"))
print(welcomeString.endswith("to", 4, 10))
str1 = "Devanshu is a good boy. He lives in Rajkot. He is a good engineer"
print(str1.find("ishh"))  # This method gives -1 if substrng is not found
# Gives error and program is terminated if substring not found
# print(str1.index("ishh"))
a = "devanshu"
print(a.isalnum())
print(a.isalpha())
print(a.isupper())
print(a.islower())
print(a.istitle())
a = "24"
print(a.isdecimal())
print(a.isnumeric())
print(a.isdigit())
print(a.isprintable())
a = "cjsnvk\n"
print(a.isprintable())
print(a.startswith("devanshu"))
a = a.replace("cjsnvk", "devanshu")
print(a.startswith("devanshu"))
print(a.swapcase())  # changes the case to uppercase
