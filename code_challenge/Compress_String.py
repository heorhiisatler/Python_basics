# Compress String
def Compress_String(Str):
    list = []
    i = 1
    for s in Str:
        if Str[i] == Str[i-1]:
            list.append(s)
        else:
            break
        i += 1
    print(list)


Compress_String("aaabbbccc")