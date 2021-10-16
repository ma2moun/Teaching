# This program is to practice while loops

# first: a for loop
# for i in range(1,11, 2):
#     print(i)
# second: a while loop


# mykey = random.randint(0,10)
# myguess = int(input("Please enter your guess: "))
#
# while True:
#     if myguess == mykey:
#         print("Correct Key! Bye!")
#         break
#     else:
#         myguess = int(input("Wrong Key! Try Again: "))
#
# For loop
# for i in range(5):  # From zero to 4 (5 numbers), each time, add 1
# #     print(i)
# mykey = random.randint(0,10)   # RANDOM!
# myguess = int(input("Please enter your guess: "))
# while True:
#     if myguess == mykey:
#         print("Correct Key, Bye!")
#         break
#     else:
#         myguess = int(input("Wrong! Try Again: "))
#


# This line will read key from file

print("Hello, What would you like to do? ")
choice = input("For encryption press 1, for decryption press 2, to exit press 0: ")
if(choice == 1):
    #call encryption function




def xor_crypt_string(data, key):
    from itertools import izip, cycle
    import base64
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored

def read_input():
    f = open("input.txt", "r")
    for line in f:
        variable = line
    ID = variable[0]
    name = variable[1]
    message = variable[2]
    create_key(ID, name)

def create_key(ID, name):
    #.....
    write_key(key)

def write_key(key):
    f = open("key.txt", "w")
    f.write(key)
    f.close()



