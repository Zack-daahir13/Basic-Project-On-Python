def revarse (qoraal):
    v = ""
    for k in qoraal:
        v = k + v
        
    return v
n = revarse("python")
print(n)

exit()
def vowel (text):
    vowels = "aeiou"
    none_vowels = ""
    for c in text:
        if c.lower() not in vowels:
            
            none_vowels+= c
    return none_vowels
var = vowel("this is zAck")
print(var)

















exit()

def vowel_count(text):
    vowels = "aeiou"
    count = 0
    for c in text:
        if c.lower() in vowels:
            count = count+1
    return count
var = vowel_count("this is the main idea of python")
print(var)



