# A Python script that asks the user whether he wants to write to a file
# or read from a file. If the user chose to read from a non-existing file, he will
# be asked to write it first.

def write_to_file():
    name = input("What is the name of the file you want to write to? (no extension required) ")
    myfile = open(name+".txt", "w")
    myfile.close()
    print("File has been created successfully!")

choice = input("Do you want to read from a file or write to a file? \n"
               "(write R for reading, W for writing): ")

if choice == 'R':
    try:
        name = input("What is the name of the file you want to read? (no extension required) ")
        myfile = open(name+".txt", "r")
        print(myfile.readlines())
        myfile.close()
    except:
        print("file doesn't exist, create the file first.\n"
              "would you like to create one? (Y/N): ")
        c = input("(Y)es or (N)o")
        if c == 'Y':
            write_to_file()
        else:
            exit()

elif choice == 'W':
    write_to_file()
else:
    print("Invalid choice!")
