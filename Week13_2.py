# Make sure that a text file exists in the same
# pathway as this script
# If not, the script will warn you.

try:
    myfile = open('test.txt', "r")  # Change the name of the file to reflect the name of the file you have
    print(myfile.readline())
except:
    print("File Doesn't Exist!, Check the Path")
