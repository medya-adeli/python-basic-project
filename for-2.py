n = 10

for i in range(n - 1):
    for j in range(i, n - 1):
        print(" ", end="")
    for j in range(i):
        if j == 0 or j == i - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i, n - 1):
        print(" ", end="")
    for j in range(i):
        if j == 0 or j == i - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
