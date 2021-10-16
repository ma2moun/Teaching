#Week 4 Exercises:
# Average Calculator

def converter(decimal):
     return bin(decimal)

dec = input("Please enter a decimal number: ") #Built-in function that takes input from the user
dec = int(dec) #Try to remove this line
binary = converter(dec) #Function Call
print(binary.replace("0b", "")) #The replace will remove the 0b from the binary number
