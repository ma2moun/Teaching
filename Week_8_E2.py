# Gussing game: infinity while

number = 99

while True:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Correct Key, Bye!")
        exit()
    else:
        print("Wrong Key, Try Again! ")

