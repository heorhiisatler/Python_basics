def is_anagram(Str1, Str2):
    list_s1 = []
    list_s2 = []
    for s in Str1:
        list_s1.append(s)
    for s in Str2:
        list_s2.append(s)
    list_s1.sort()
    list_s2.sort()
    if list_s1 == list_s2:
        return True
    else:
        return False


s1 = input("enter string1: ")
s2 = input("enter string2: ")
print(is_anagram(s1, s2))
