def get_row_col(Str1):
    match Str1:
        case "A1":
            return (0, 0)
        case "A2":
            return (1, 0)
        case "A3":
            return (2, 0)
        case "B1":
            return (0, 1)
        case "B2":
            return (1, 1)
        case "B3":
            return (2, 1)
        case "C1":
            return (0, 2)
        case "C2":
            return (1, 2)
        case "C3":
            return (2, 2)









while True:
    s1 = input("enter string: ")
    if s1 == "q" or s1 == "quit": break
    print(get_row_col(s1))