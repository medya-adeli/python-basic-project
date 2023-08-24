i = 1
s = int(input("Enter a number: "))
while i <= s:
    spaces = i
    stars = s - i
    if i==1:
        print("*")

    while spaces > 0:  
        print(" ", end="")
        spaces -= 1

    while stars > 0:  
        print("*", end="")
        stars -= 1

    print()  
    i += 1
