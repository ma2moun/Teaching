try:
    myfile = open("test.txt", "r")
except:
    print("No file was found!")
finally:
    print(myfile.readlines())
##    for line in myfile:
##        print(line)

myfile.close()  #You may use the "with" way which will close the file automatically
