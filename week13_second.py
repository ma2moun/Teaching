#Read multiline using a loop!

#First function is to append muliple lines to a textfile
def append_lines():
     i = 1
     with open("mytext.txt", "a") as myfile:
          for i in range(3):
               variable = input("What would you like to write to this line: ")
               myfile.writelines(variable+"\n")
     read_file()

def read_file():
     with open("mytext.txt", "r") as myfile:
          for line in myfile:
               print(line)


append_lines()
