#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number.

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
