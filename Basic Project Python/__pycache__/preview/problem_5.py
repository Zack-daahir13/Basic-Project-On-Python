#problem 5-Digits in Order List

def digits_in_order(number):
    return [int(digit) for digit in str(number)]

#user take me as input
user_input = int(input("Enter a non-negative integer: "))

# Call the function and print the result
result = digits_in_order(user_input)
print("List of digits:", result)
