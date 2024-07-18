print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ") 
add_pepperoni = input("Do you want pepperoni? Y or N") 
extra_cheese = input("Do you want extra cheese? Y or N")
bill = 0

# Determine the base cost based on the size
if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
elif size == "L":  # Ensure we handle the case for "L" specifically
    bill = bill + 25

# Add cost for pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:  # For M and L sizes
        bill = bill + 3

# Add cost for extra cheese
if extra_cheese == "Y":
    bill = bill + 1

# Print the final bill
print(f"Your final bill is: ${bill}.")
