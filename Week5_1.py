#Simple if statement:


x = input("Enter Your Age: ")
x = int(x)

if x>=18:
     print("You can get a license")
else:
     print("Sorry, you cannot get a license. You still need ", 18-x, " years to get it")
     
