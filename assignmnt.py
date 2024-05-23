
# Prompt the user for hours and rate per hour
hours = input("Enter hours worked: ")
rate_per_hour = input("Enter rate per hour: ")

# Convert the input strings to floats
hours = float(hours)
rate_per_hour = float(rate_per_hour)

# Compute the gross pay
gross_pay = hours * rate_per_hour

# Print the computed gross pay
print("Pay:", gross_pay)
