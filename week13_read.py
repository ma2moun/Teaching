#This will read from a text file.

def read_file(filename):
     try:
          myfile = open(filename+".txt", "r")  # r means reading!
          var1 = myfile.readlines()
          ID = var1[0]
          name = var1[1]
          message = var1[2]
          print(message)
          myfile.close()
     except:
          print("file doesn't exist")


filename = input("Please enter the file name: ")
read_file(filename)
