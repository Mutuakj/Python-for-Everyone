# Prompt the user to enter the score
score = input("Enter score:")
score = float(score)

# Check if the score is within the valid range
if score < 0.0 or score > 1.0:
    print("Error: Score is out of range.")
else:
    # Determine the grade based on the score
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    # Print the grade
    print(grade)
