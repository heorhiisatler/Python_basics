def rev_str(Str):
    Str_rev = ""
    i = len(Str) - 1
    while (i >= 0):
        Str_rev += Str[i]
        i -= 1
    return(Str_rev)


s1 = input("enter string: ")
print(rev_str(s1))