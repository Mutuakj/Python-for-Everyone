def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        regular_pay = 40 * r
        overtime_pay = (h - 40) * (r * 1.5)
        return regular_pay + overtime_pay

# Prompt the user for input
hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate per Hour: "))

# Calculate the pay using the computepay function
p = computepay(hrs, rate)

# Display the result
print("Pay", p)
