while True:
    x = input("Enter a number what count to: ")
    if x == "q" or x == "quit":
        break
    y = 1
    while True:
        if y > int(x):
            break
        print(y)
        y = y + 1
