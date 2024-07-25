# Input a list of student scores
student_scores = input('Enter the Scores: \n').split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Initialize variables
score = 0
highest_score = 0

# Calculate total score and find highest score
for n in student_scores:
    score += n  # Add each score to the total score
    if n > highest_score:
        highest_score = n  # Update highest_score if current score is higher

# Print the highest score outside the loop
print(f"The highest score in the class is: {highest_score}")
