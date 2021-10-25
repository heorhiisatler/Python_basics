def add_dots(Str):
    Str2 = ""
    i = 0
    for s in Str:
        if i < (len(Str)-1):
            Str2 = Str2 + s + "."
        i = i + 1
    else:
        Str2 = Str2 + s
    return Str2


def remove_dots(Str):
    Str3 = ""
    for s in Str:
        if s != ".":
            Str3 = Str3 + s
    return Str3


s1 = input("enter string: ")
print(add_dots(s1))
print(remove_dots(add_dots(s1)))
