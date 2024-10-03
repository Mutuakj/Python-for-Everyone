# Prompt user to input the numbers
first_number = int(input('Please enter a whole number greater than 1: '))
second_number = int(input(f"\nPlease enter another number, greater than {first_number}: "))

# Check if the first number is greater than 1
if first_number < 1:
    print('\nERROR! The first number is less than or equal to 1. Try again.')
    
    # Check if second number is greater than the first number
elif second_number < first_number:
    print(f"\nERROR! The second number is less than or equal to {first_number}. Try again.")

else:
    # Find the product of all integers between the 2 numbers
    def product_of_range(first_number, second_number):
        product = 1
        for number in range(first_number, second_number + 1):
            product *= number
        return product
result = product_of_range(first_number, second_number)
print(f"\nThe product of all integers from {first_number} to {second_number} is: {result}")





