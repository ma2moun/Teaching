age= input("please enter your age: ")
age= int (age)

message1 = "Congratulations, you are eligible to obtain a driving license!"
message2 = "Unfortunately, you cannot obtain a license now, you still have ",18-age," years to be able to 18"
print(message1 if age>=18 and age<=100 and age>0   else message2)
