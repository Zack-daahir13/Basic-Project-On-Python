#problem 1- Removing minimum number

def remove_minimum_number(numbers):
    return [n for i, n in enumerate(numbers) if i != numbers.index(min(numbers))]

# Take me user as input
user_input = input("Enter a list of numbers separated by spaces: ")
user_numbers = [int(x) for x in user_input.split()]

# Call the function and print the result
result = remove_minimum_number(user_numbers)
print("Modified list:", result)
