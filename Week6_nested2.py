#  Example 2: Finding wether a given number is divisable by two and three


num = int(input("Please enter any number: "))
if num%2 == 0:
   if num%3 == 0:
      print (num, " is divisible by 3 and 2")
   else:
      print (num, " is divisible by 2 and not divisible by 3")
else:
   if num%3 == 0:
      print (num, " is divisible by 3 and not divisible by 2")
   else:
      print  (num, " is not divisible by 2 and not divisible by 3")
