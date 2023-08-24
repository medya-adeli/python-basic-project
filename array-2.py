###############Start of first slution#####################
def mathfun():
    x=int(input("enter number:"))
    y=int(input("enter number:"))
    z=int(input("enter number:"))
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    c=int(input("enter number:"))
    d=int(input("enter number:"))
    e=int(input("enter number:"))
    f=int(input("enter number:"))
    g=int(input("enter number:"))
    arr = [x,y,z,a,b,c,d,e,f,g]
    x=arr.count(2)
    return(x)
print(mathfun())
###############End of first slution#####################
########################################################
###############Start of second slution#####################
def mathfun():
    x = int(input("enter number:"))
    y = int(input("enter number:"))
    z = int(input("enter number:"))
    a = int(input("enter number:"))
    b = int(input("enter number:"))
    c = int(input("enter number:"))
    d = int(input("enter number:"))
    e = int(input("enter number:"))
    f = int(input("enter number:"))
    g = int(input("enter number:"))
    arr = [x, y, z, a, b, c, d, e, f, g]
    count = 0

    if x == 2:
        count += 1
    elif y == 2:
        count += 1
    elif z == 2:
        count += 1
    elif a == 2:
        count += 1
    elif b == 2:
        count += 1
    elif c == 2:
        count += 1
    elif d == 2:
        count += 1
    elif e == 2:
        count += 1
    elif f == 2:
        count += 1
    elif g == 2:
        count += 1

    print(f"Number of 2s: {count}")

mathfun()

################End of second slution#####################


