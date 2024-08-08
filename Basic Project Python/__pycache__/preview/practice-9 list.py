def remove_empty_string():
    strings = input("Enter a list of strings, separated by spaces: ").split()
    filtered_list = [string for string in strings if string.strip()]
    return filtered_list

result = remove_empty_string()
print("Filtered List:", result)
exit()
#problem 1
def calculate_sum():
    numbers = input("Enter a list of numbers, separated by spaces: ").split(",")
    numbers = [int(num) for num in numbers]
    return sum(numbers)
result = calculate_sum()
print("Sum:", result)

#problem 2
def square_list_items():
    numbers = input("Enter a list of numbers, separated by commas: ")
    numbers = [int(num) for num in numbers.split("," )]
    squared_list = [num ** 2 for num in numbers]
    return squared_list

result = square_list_items()
print("Squared List:", result)

#problem3
def remove_empty_string():
    strings = input("Enter a list of strings, separated by spaces: ").split()
    filtered_list = [string for string in strings if string.strip()]
    return filtered_list

result = remove_empty_string()
print("Filtered List:", result)

#problem4
def remove_duplicates():
    elements = input("Enter a list of elements, separated by spaces: ").split()
    unique_elements = list(set(elements))
    return unique_elements

result = remove_duplicates()
print("Updated List:", result)

#problem 5
def have_common_members():
    list1 = input("Enter the first list of elements, separated by spaces: ").split()
    list2 = input("Enter the second list of elements, separated by spaces: ").split()

    common_members = set(list1) & set(list2)
    return len(common_members) > 0

result = have_common_members()
print("Common Members Exist:", result)

#problem 6
def reverse_list():
    elements = input("Enter a list of elements, separated by spaces: ").split()
    reversed_list = list(reversed(elements))
    return reversed_list
result = reverse_list()
print("Reversed List:", result)