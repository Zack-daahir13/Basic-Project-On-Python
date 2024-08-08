#problem-2 removing every second item
def remove_second_element(input_list):
    return input_list[::2]

# Take user input
user_input = input("Enter a list of elements separated by spaces: ")
user_list = user_input.split()

# Call the function and print the result
result = remove_second_element(user_list)
print("Modified list:", result)
