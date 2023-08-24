def validate():
    try:
        shopping = int(input("Enter more than 10,000: "))
        if shopping >= 10000:
            return shopping
        else:
            print("Invalid input! Amount should be 10,000 or more.")
            return validate()  
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return validate()  


first_thing = validate()
second_thing = validate()
third_thing = validate()
fourth_thing = validate()

percentage = 5
total_amount = first_thing + second_thing + third_thing + fourth_thing

if total_amount > 100000:
    reduction_amount = (total_amount * percentage) / 100
    result = total_amount - reduction_amount
    print("---------------------------------------------")
    print("First edition:", total_amount)
    print("---------------------------------------------")
    print("Discount:", reduction_amount)
    print("---------------------------------------------")
    print("Result:", result)
else:
    print(f"Your total shopping amount is:{total_amount}")
