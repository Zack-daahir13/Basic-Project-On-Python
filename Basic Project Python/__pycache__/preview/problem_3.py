#problem-3 unsorted increment lists

def incrementing_list(input_list):
    min_value = min(input_list)
    max_value = max(input_list)
    return list(range(min_value, max_value + 1))

# Take me user as input
user_input = input("Enter a list: ")
user_list = [int(x) for x in user_input.split()]

# Call the function 
result = incrementing_list(user_list)
print("Incrementing list:", result)
