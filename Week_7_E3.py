# To print a Pyramid of stars
# Function to demonstrate printing pattern triangle


def pyramid(length):
    # Calculate the number of spaces
    spaces = 2 * length

    # outer loop to handle number of rows in the pyramid
    for i in range(0, length*2):

        # inner loop to handle number spaces for each row of the pyramid
        for j in range(0, spaces):
            print(end=" ")
            # decrementing the number of spaces after each loop
        spaces = spaces - 1

        # inner loop to handle number of columns
        for j in range(0, i + 1):
            # printing the stars
            print("* ", end="")

            # ending line after each row
        print("\n")


name = input("Please enter your name: ")
length = len(name)

pyramid(length)


