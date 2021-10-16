#Exercise 5.4

age= input("Please enter your age: ")
ID = input("Please enter your student ID: ")
age=int(age) #convert from str to int

last3 = ID[-3:] #To stip the last 3 digits of the ID
sum3 = int(last3[-3:-2]) + int(last3[-2:-1])+int(last3[-1:]) #to sum the last 3 digits of the ID

print("The sum of the last 3 digits of your ID is: ",sum3)

if sum3>age:
     print("Your ID is greater than your age")
elif sum3==age:
     print("What a lucky!")
else:
     print("Your ID is less than your age")
