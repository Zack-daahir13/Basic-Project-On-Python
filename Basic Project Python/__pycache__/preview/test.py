def swap_cases(input_str):
    return input_str.swapcase()
swap_cases(input("enter a word: "))
exit()
# Example usage with user input:
input_str = input("Enter a string: ")
result = swap_cases(input_str)
print(result)
exit()
#problem1
def calculate_sum_and_average(input_str):
    digits = [int(char) for char in input_str if char.isdigit()]
    digit_sum = sum(digits)
    digit_count = len(digits)
    average = digit_sum / digit_count if digit_count > 0 else 0
    return f"Sum is: {digit_sum}, Average is {average}"

# Example usage with user input:
input_str = input("Enter a string: ")
result = calculate_sum_and_average(input_str)
print(result)
#problem2

import re

def remove_special_symbols(input_str):
    modified_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
    return modified_str

# Example usage with user input:
input_str = input("Enter a string: ")
result = remove_special_symbols(input_str)  
print(result)

#problem 3
def swap_cases(input_str):
    return input_str.swapcase()

# Example usage with user input:
input_str = input("Enter a string: ")
result = swap_cases(input_str)
print(result)


#problem4

def count_occurrences(text, substring):
    return text.lower().count(substring.lower())

# Take user input
text = input("Enter the text: ")
substring = input("Enter the substring to search: ")

result = count_occurrences(text, substring)
print(f"{substring} appears {result} times")