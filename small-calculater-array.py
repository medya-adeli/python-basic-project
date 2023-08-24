arr = ['*', '/', '+', '-']

def func():
    while True:
        try:
            x = input("Enter the first number: ")
            y = input("Enter the second number: ")
            z = int(input("Enter the operator in range (0 to 3): 0: *, 1: /, 2: +, 3: -: "))

            if 0 > z > 3:
                print("Invalid operator index. Please choose an operator index between 0 and 3.")
            else:
                break  
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    result = eval(x + arr[z] + y)

    print("---------------------")
    print("The answer is:", result)
    print("---------------------")

func()
