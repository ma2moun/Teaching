# a program that creates a unique number from your fall name.
alphabet = " abcdefghijklmnopqrstuvwxyz"
name = input("Please enter your full name: ")
name = name.lower()
unique = 0
for c in name:
    unique += alphabet.index(c)
print("Your unique number is: ", unique)