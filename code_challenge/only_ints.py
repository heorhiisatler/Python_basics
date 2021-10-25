#only_ints
def only_ints(a,b):
    if type(a) == type(b):
        return True
    else:
        return False

print(only_ints(1,"b"))