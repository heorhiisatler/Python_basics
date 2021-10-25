def mid(Str):
    i = 0
    list = []
    for s in Str:
        list.append(s)
        i = i + 1     
    print(list)
    if (i % 2) == 0:
        return ""
    else:
        return list[int((i/2)-0.5)]


s1 = input("enter string: ")
print(mid(s1))