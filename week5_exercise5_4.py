# This is the solution of exercise 5.4
# In this program, we compare the last 3 digits of my ID
# with my age, and based on that, the program will take decision


age = int(input("Please enter your age: ")) #To input age
SID = input("Please enter your SID: ") #to input SID

Total  = int(SID[-1:]) + int(SID[-2:-1]) + int(SID[-3:-2]) #To sum up the last 3 digits


if Total > age:
     print("ID is greater than age")
elif Total ==age:
     print("What a lucky!")
else:
     print("Your ID is less than your age.")



