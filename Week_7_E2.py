# A program that asks for the student ID, and then sums up the digits using a for loop

sid = input("Please enter your SID: ")
summation = 0
for c in sid:
    summation += int(c)
print(summation)