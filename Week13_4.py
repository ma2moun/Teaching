"""a Python script that asks the user to create a file (file write),
however, the script must also ask the user to input the name of the file
using input function. Then it will ask the user about the content that should
be written to that file."""


def write_to_file():
    name = input("What is the name of the file you want to write to? (no extension required) ")
    myfile = open(name+".txt", "w")
    message = input("What would you like to write to this file? \n")
    myfile.write(message)
    myfile.close()
    print("File has been created successfully!")

write_to_file()
