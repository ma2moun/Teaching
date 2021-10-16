# Gussing game: infinity while, using random function to generate a number
import random  # This will import the random library


def create_random():
    number = random.randint(0, 10)
    return number


while True:
    mytry = 1
    number = create_random()
    while mytry <= 3:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print(f"Correct key in {mytry} attempts, Bye!")
            exit()
        else:
            print("Wrong Key, this is your attempt number ", mytry)
        mytry += 1


