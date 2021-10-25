#Counting syllables
def count(Str):
    syl_count = 0
    for s in Str:
        if s == "-": syl_count = syl_count + 1
    return syl_count + 1

s1 = input("enter string: ")
print(count(s1))