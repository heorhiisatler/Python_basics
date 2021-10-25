def capital_indexes(Str):
    list = []
    i = 0
    for s in Str:
        if s.isupper():
            list.append(s)
        i = i + 1
    return list


s1 = input("enter string: ")
print(capital_indexes(s1))
