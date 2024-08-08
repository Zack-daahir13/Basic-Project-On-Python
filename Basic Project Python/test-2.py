while True:
    height = input("number: ").strip()
    if height.isalpha() or int(height) < 1 or int (height)>8:
        continue
    else:
        break
    height = int(height)
    
    


def mario():
    while True:
        try:
            height = int(input("Enter the height of the pyramid (1-8): "))
            if height < 1 or height > 8:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer between 1 and 8.")

    # Print the pyramid pattern
    for i in range(height):
        # Print spaces
        print(" " * (height - i - 1), end="")

        # Print hashes
        print("#" * (i + 1))

def mario():
    while True:
        try:
            height = int(input("Enter the height of the pyramid (1-8): "))
            if height < 1 or height > 8:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer between 1 and 8.")

    # Print the pyramid pattern
    for i in range(height):
        # Print spaces
        print(" " * (height - i - 1), end="")

        # Print hashes
        print("#" * (i + 1))
        
def mario():
    while True:
        try:
            height = int(input("Enter the height of the pyramid (1-8): "))
            if height < 1 or height > 8:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer between 1 and 8.")

    # Print the pyramid pattern
    for i in range(height):
        # Print spaces
        print(" " * (height - i - 1), end="")

        # Print hashes
        print("#" * (i + 1))
        
mario()

mario()
    
mario()

def mario():
    while True:
        try:
            height = int(input("Enter the height of the pyramid (1-8): "))
            if height < 1 or height > 8:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a positive integer between 1 and 8.")
        else:
            break

    # Print the pyramid pattern
    for i in range(height):
        # Print spaces
        print(" " * (height - i - 1), end="")

        # Print hash
        print("#")

mario()

exit()
for i in range(1,6):
    for j in range(i):
      print("#", end="")
print()
    
        
