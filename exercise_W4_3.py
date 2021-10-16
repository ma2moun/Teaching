def dec_to_bin(decimal):
     return bin(decimal)


dec = input("Please enter a decimal number: ") #built-in function
dec = int(dec) #To convert to integer
result = dec_to_bin(dec) #Function call to convert to binary
print(result.replace("0b", "")) #to remove the 0b from the binary number

