# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Equal to or over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.
# Enter your height in meters e.g., 1.55
#height = float(input())
# Enter your weight in kilograms e.g., 72
#weight = int(input())
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

height = float(input("Enter the height "))
weight = int(input("Enter the weight "))
#print(type(height))
#print(type(weight))

bmi = weight/(height*height)
bmii = int(bmi)


if bmii < 18.5:
 print(f"Your BMI is  {bmii}, you are underweight.")
elif bmii >= 18.5 and  bmii< 25:
 print(f"Your BMI is  {bmii}, you have a normal weight.")
elif bmii >=25 and bmii < 30:
  print(f"Your BMI is  {bmii}, you are slightly overweight. ")
elif bmii >=30 and bmii < 35: 
  print(f"Your BMI is  {bmii}, you are obese.")
else:
 if bmii >=35:
  print(f"Your BMI is  {bmii}, you are clinically obese.")

  
  
  #OR
  
#   bmi = weight/(height*height)
# if bmi < 18.5:
#  print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#  print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight. ")
# elif bmi < 35: 
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi} you are clinically obese.")





