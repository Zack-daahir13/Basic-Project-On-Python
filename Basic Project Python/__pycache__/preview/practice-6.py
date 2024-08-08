#2 string problems
#1- Remove first and last chracter
def totall(x, y, z):
    print(x + y + z)
totall(10, 10, 10)

def get_length(taxes):
    return len( taxes)
print(get_length("zack"))

#another proplem
def replace_char(text, char, new_char):
    if char in text:
        new = text.replace(char, new_char)
        return new
    else:
        return("the chracter isn\'t found")
print(replace_char("python", "w", "$"))

#another problem
def badalid(text):
    if text[0] == text[0].upper():
        return text.upper()
    else:
        return text.lower()
print(badalid("Zack"))


exit()
    
def p1(name, ptch):
    print(F"your name is: {name}and yout batch is {ptch}")
print(p1("zack"))
print(p1("4"))


def removing(name):
    x = ""
    for i in name:
        x = x + i  
    return x
name1= removing(input("enter the word: "))
print(name1[1:4])
name1= removing(input("enter the word: "))
print(name1[1:5])
name1= removing(input("enter the word: "))
print(name1[1:5])
name1= removing(input("enter the number: "))
print(name1[1:4])
name1= removing(input("enter the word: "))
print(name1[1:6])

#problem 2- Get the middle chracter (s)

def middle_names(name):
    n = ""
    for x in name:
        n = n + x
    return n

print("this problem 2 is get the middle chracter")
output = middle_names(input("enter the four latter: "))
print(output[1:3])
output = middle_names(input("enter the numbers: "))
print(output[3])
output = middle_names(input("enter the letters: "))
print(output[2:4])
output = middle_names(input("enter the letters: "))
print(output[3])
output = middle_names(input("enter the letters: "))
print(output[3])