print("Welcome to Python")
value = input("Enter your integer value: ")
print("Your Entered Integer value is: "+value+"")
name = ["Abdul","Hameed","Bathusha","Mohamed","Yousuf"]
print(len(name))
i = 0
for x in name:
    print(x)
    print(x.upper())
while i < len(name)-2:
    print(name[i].lower())
    i=i+1
print(name)