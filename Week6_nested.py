# A simple guessing application using nested if:


guess = int(input("Please enter a number between 0 and 50: "))
if guess < 50:
   print ("Your guess is below 50, ")
   if 10>guess>=0:
      print("and it is between 0 and 10")
   elif 20>guess>=10:
      print("and it is between 10 and 20")
   elif 30>guess>=20:
      print ("and it is between 20 and 30")
   elif 40>guess>=30:
      print ("and it is between 30 and 40")
   elif 50>guess>=40:
      print ("and it is between 40 and 50")
else:
   print("Your number is not between 0 and 50")

print ("Good bye!")
