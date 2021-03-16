import re
def countConsonants(str):
    cnt = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    str1= list(str)
    for i in str1 :
        if i in vowels :
            continue
        else :
            cnt += 1
    return cnt
str = input("Enter a string :")
if not re.match("^[a-zA-Z ]*$", str) :
    print("Enter valid string")
else :
    a = countConsonants(str)
print(a)
    
