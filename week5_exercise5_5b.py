#Comments etc....


#This program is to win money depending on your age and ID number

choice = bool(input("Do you have an ID? (True or False): ")) #Yes or NO
if choice == "True":
     ID=input("Please enter your ID : ")
     
Age=int(input("Please enter you age: "))
X=int(ID[-1:]) #To convert to integer

if (Age == 18 or Age == 19) and X % 2 == 0:
    print("You win", X, "Riyals")

elif (Age == 18 or Age == 19) and X % 2 != 0:
    print("You win", X/2, "Riyals")

elif (Age>19 or Age<=22) and X % 2 != 0:
    print("You win", X,X ,"Riyals")

elif (Age>19 or Age<=22) and X % 2 == 0:
    print("You win", X, X, X, "Riyals")

elif Age > 22 or choice == False:
    print("You owe us 500 Riyals")
