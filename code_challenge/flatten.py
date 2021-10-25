def flatten(Lst_x2):
    Lst_x1 = []
    for L1 in Lst_x2:
        for L2 in L1:
            Lst_x1.append(L2)
    return Lst_x1


print(flatten([ [1, 2], [3, 4] ]))