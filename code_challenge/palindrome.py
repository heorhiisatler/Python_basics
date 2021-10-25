#commit from CT
def palindrome(Str):
    list_fwd = []
    list_rws = []
    i = len(Str) - 1
    for s in Str:
        list_fwd.append(s)
        list_rws.append(Str[i])
        i -= 1
    if list_fwd == list_rws: return True
    else: return False
    #print(list_fwd)
    #print(list_rws)

s1 = input("enter string1: ")
print(palindrome(s1))        
