#     """def ms(number1, number2):
#         prod = number1 * number2
#         if prod <= 1000:
#             return prod
#         else:
#             return number1 + number2

# result = ms(20,30)
# print("The result is = ", result)


# result = ms(40,30)
# print("The result is = ", result)"""




#     """number = list(range(10))
#     pnumber = 0
#     for i in number:
#         sum = pnumber + i
#         print('Current Number '+ str(i) + ' Previous Number ' + str(pnumber) + ' is ' + str(sum))
#         pnumber=i"""




# """word = input('Enter a word ')
# print("Actual String:", word)

# a = list(word)
# for i in a[0::2]:
#     print(i)"""


# def rem_chars(word, n):
#     print('Actual string:', word)
#     a = word[n:]
#     return a

# print("Removing characters from a string")
# print(rem_chars("pynative", 4))
# print(rem_chars("pynative", 2))





#     def get_choices():
#         player_choice = "rock"
#         computer_choice = "paper"





# """def first_number(numberList):
#     print("Given list:", numberList)
    
#     first_number = numberList[0]
#     last_number = numberList[-1]
    
#     if first_number == last_number:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_number(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_number(numbers_y))"""



# """num_list = [10, 20, 33, 46, 55]
# print("Given list:", num_list)
# print('Divisible by 5:')
# for i in num_list:
#     if i % 5 == 0:
#         print(i)"""


# """str_x = "Emma is good developer. Emma is a writer"
# c = str_x.count("Emma")
# print(c)"""


# """for num in range(6):
#     for i in range(num):
#         print (num, end=" ") 
#     print("\n")"""

# """def palindrome(number):
#     print("Actual number", number)
#     original_num = number
    
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10

   
#     if original_num == reverse_num:
#         print("Yes. Given number is palindrome number")
#     else:
#         print("No. Given number is not a palindrome number")

# palindrome(121)
# palindrome(125)"""




# """for i in range(6, 0, -1):
#     for a in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")"""

# while True:
#  print('Please type your name.')
#  name = input()
#  if name == 'your name':
#   break
# print('Thank you!')


# name = ''
# while not name:
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
#  print('Be sure to have enough room for all your guests.')
# print('Done')
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)

# age = input("Enter your age\n")
# your_years = 60 - int(age)
# left = your_years * 52;
# print(f"Your left with {left} weeks")
# print(type(age))
# print(type(your_years))

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("WELCOME TO THE TIP CALCULATOR")
bill_amt = float(input("Please provide the bill: $ "))
tip = int(input("Choose your tip? 10, 12, 15?: "))
people = int(input("How many of you sharing: "))
tip_percentage = tip / 100
total_tip = tip_percentage * bill_amt
total_bill = bill_amt + total_tip
total_bill_per_person = total_bill / people
final_bill = round(total_bill_per_person,2)
final_bill = "{:.2f}".format(total_bill_per_person)
print(f"The final bill for each person is {final_bill}")
