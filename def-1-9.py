a = []
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
index = 0

def chlist():
    global count, index
    
    while len(a) <= 10:
        x = int(input("Enter: "))
        a.append(x)
        print(a)
    
    while index < len(a):
        if a[index] == 1:
            count[0] += 1
        elif a[index] == 2:
            count[1] += 1
        elif a[index] == 3:
            count[2] += 1
        elif a[index] == 4:
            count[3] += 1
        elif a[index] == 5:
            count[4] += 1
        elif a[index] == 6:
            count[5] += 1
        elif a[index] == 7:
            count[6] += 1
        elif a[index] == 8:
            count[7] += 1
        elif a[index] == 9:
            count[8] += 1
        elif a[index] == 10:
            count[9] += 1
        index += 1
    
    print("Count of number 1:", count[0])
    print("Count of number 2:", count[1])
    print("Count of number 3:", count[2])
    print("Count of number 4:", count[3])
    print("Count of number 5:", count[4])
    print("Count of number 6:", count[5])
    print("Count of number 7:", count[6])
    print("Count of number 8:", count[7])
    print("Count of number 9:", count[8])
    print("Count of number 10:", count[9])

chlist()
