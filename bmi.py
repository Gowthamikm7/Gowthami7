height = float(input("Enter the height "))
weight = int(input("Enter the weight "))
# print(type(height))
# print(type(weight))

bmi = weight/height**2
bmi = weight/(height*height)
bmii = int(bmi)
print("Your bmi calculation is : " + str(bmii))

