#Problem 4 Word Length and Append List

def word_length_and_append(input_string):
    words = input_string.split()
    result = [f"{word} {len(word)}" for word in words]
    return result

# Take me user as input
user_input = input("Enter a string of words: ")

# Calling the function
result = word_length_and_append(user_input)
print("Modified list:", result)
