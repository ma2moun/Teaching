#Exercise 5.5

age= input("Please enter your age: ")
ID_exist = input("Do you have a student ID? (yes/no): ")
if ID_exist=='yes':
     ID = input("Please enter your student ID: ")
else:
     ID='0'
age=int(age) #convert from str to int

last = ID[-1:] #To stip the lastdigit of the ID
last = int(last) #convert to int

#print(ID_exist)

if (age==18 or age==19) and ID_exist=='yes':
     if last%2==0: #even
          print("You win ", last, " Riyals")
     else:
          print("You win ", last/2," Riyals")
elif (age>19 and age<=22) and ID_exist=='yes':
     if last%2==0:
          last=str(last) #optional to print the last 3 times before spaces (can be last,last,last)
          print("You win ",last*3, " Riyals")
     else:
          last=str(last)
          print("You win ",last*2, " Riyals")
elif age>22 or ID_exist=='no':
     last=str(last)
     print("You owe us ",last*4, " Riyals")

