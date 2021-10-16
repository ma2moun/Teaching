#this program is to practice If statements

age = input("Please enter your age: ") #To input age from users
age = int(age) #to convert from str to int


message1 = "Congratulations, you are eligible to obtain a driving license!"
message2 = "Sorry! you cannot obtain a license, you can do it in ", 18-age, " years from now"
message3 = "For your safety, you are not eligible for driving, we cannot renew your license!"


print(message1 if 75>=age>=18 else message3 if age>75 else message2)



#TODO:
     
#UPDATE THIS TO TELL PEOPLE WHO ARE ABOVE 75
     #THAT THEY CANNOT RENEW THEIR LICENSES
     #BECAUSE OF THEIR SAFETY

