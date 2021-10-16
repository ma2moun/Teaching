# Reverse the name

name = input("Please enter your name: ")
length = len(name)
for char in range(length):
    if length != 0:
        print(name[length-1])
    length -= 1


