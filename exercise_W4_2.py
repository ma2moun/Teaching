#this will calculate the average of 5 marks

#First function to sum up numbers:


def summation (x,y,z,r,s):
     print("The sum of numbers is: ", x+y+z+r+s)
     return (x+y+z+r+s)


def average(sum1):
     print("The average of marks is: ", sum1/5)


out = summation(65,70,90,81,100)

average(out)


