a = int(input('Enter a number: '))
b = 1
while a >= b:
    s = b
    while s > 0:
        print(' ', end=" ")
        s -= 1
    print('*_*')
    s = b
    while s > 0:
        print(' ', end=" ")
        s -= 1
    print(' O')
    b += 1
