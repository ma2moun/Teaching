# This program will read the content of a text file (.txt)

def create_file(filename):
     newfile = open(filename+".txt", "w")
     newfile.writelines("Good Morning!\n")
     newfile.writelines("MTCS4005\n")
     newfile.writelines("Computer Systems!")
     newfile.close()


filename = input("Please enter the file name (no extension is needed): ") #nf
try:
     myfile = open(filename+".txt", "r") #nf.txt
     info = myfile.readlines()
     firstline = info[0]
     secondline = info[1]
     thirdline = info [2]

     print( secondline + firstline +thirdline)
     myfile.close()
except:
     print("File Doesn't Exist! Now it is being created!")
     create_file(filename)
