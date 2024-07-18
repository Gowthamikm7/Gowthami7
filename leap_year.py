year = int(input("Enter the year "))
if year %4 !=0:
 print("Not leap year")
else:
 if year %100 != 0:
  print("Leap year")
 elif year %400 == 0:
  print("It's a leap year")
 else:
  print("Not leap year")

# A year is a leap year if:
# It is divisible by 4.
# If it is also divisible by 100, it must be divisible by 400 to be a leap year.
# If a year is not divisible by 4, it is not a leap year.
# If a year is divisible by 4 but not by 100, it is a leap year.
# If a year is divisible by 4 and by 100, it must also be divisible by 400 to be a leap year.
