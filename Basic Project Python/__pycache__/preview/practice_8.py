#problem 1

def calculate_sum_and_average(input_str):
    digits = [int(char) for char in input_str if char.isdigit()]
    digit_sum = sum(digits)
    digit_count = len(digits)
    average = digit_sum / digit_count if digit_count > 0 else 0
    return f"Sum is: {digit_sum}, Average is {average}"

# Example usage:
input_str = input("enter word")
result = calculate_sum_and_average(input_str)
print(result)

input_str = "abc456def789"
result = calculate_sum_and_average(input_str)
print(result)

input_str = "1a2b3c4d5e6f7g8h9i0"
result = calculate_sum_and_average(input_str)
print(result)

input_str = "TestingWithSymbols&1234"
result = calculate_sum_and_average(input_str)
print(result)

#problem2

import re

def remove_special_symbols(input_str):
    modified_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
    return modified_str

# Example usage:
input_str = "Hello, World!"
result = remove_special_symbols(input_str)
print(result)

input_str = "Python:High-Level-Language."
result = remove_special_symbols(input_str)
print(result)

input_str = "Remove @Symbols#123!"
result = remove_special_symbols(input_str)
print(result)

#problem 3
def swap_cases(input_str):
    return input_str.swapcase()

# Example usage:
input_str = "Python Programming"
result = swap_cases(input_str)
print(result)

input_str = "UPPERCASE lowercase 45"
result = swap_cases(input_str)
print(result)

input_str = "uppercase"
result = swap_cases(input_str)
print(result)

input_str = "Special @Characters!"
result = swap_cases(input_str)
print(result)