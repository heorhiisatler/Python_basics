#double_letters
def double_letters(str):
    i = 0
    while i != (len(str)-1):
        if str[i] == str[i+1]:
            return True           
        i = i + 1
    return False

  
s1 = input("enter string: ")
print(double_letters(s1))