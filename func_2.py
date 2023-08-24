def func():
    arr = []
    index = 0

    while len(arr) < 10:
        x = int(input("Enter: "))
        arr.append(x)
        arr.sort()
        print(arr)
    
    while index < len(arr) - 1:
        count = 1
        while index < len(arr) - 1 and arr[index] == arr[index + 1]:
            count += 1
            index += 1
        if count > 1:
            print(f"{arr[index]}: {count}")
        index += 1

func()
