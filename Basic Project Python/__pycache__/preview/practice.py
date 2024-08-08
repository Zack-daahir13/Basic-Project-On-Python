x = input("enter a word: ")
n = "!"
if x == n:
    x.remove(n)
print(x) 

x = input("enter a word: ")
x.upper == x or x.lower == x
print(x.lower())
exit()
def iseven(n):
    if n.isalpha():
        return "please enter a number"
    if int(n) % 2==0:
        return True
    else:
        return False
    #return int(n)% 2==0
number = input("enter number: ")
print(iseven(number))

#problem 2
def check_occurance(text):
   replaced_char = text[0].lower()
   new_text = text[1: ].lower().replace(replaced_char, "%")
   return text [0] + new_text
print(check_occurance("Resturant")) 

#problem 3
def fectorial(n):
    
    n = int(n)
    if n < 0:
        print("this number is negative")
        return
    result = 1
    for i in range (n, 0, -1):
        result = result * i
    print(result)
fectorial(-5)

#problem 4

def addingorly (text):
    if len(text) <=3:
        return text
    elif text.endswith ("ing"):
        return text + "ly"
    return text + "ing"
print(addingorly("python"))
print(addingorly("on"))
print(addingorly("king"))

#problem 5

def arrange(text):
    lowercase = ""
    uppercase = ""
    for i in text:
        if i.isalpha():
            if i.islower:
                lowercase +=i
            else:
              uppercase +=i
    return lowercase + uppercase
print(arrange("HtMl"))