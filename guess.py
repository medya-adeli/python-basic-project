import random

def guess_number():
    number = random.randint(1, 100)
    guess = 0

    while guess != number:
        guess = int(input("Enter a number: "))

        if guess > number:
            print("Lower")
        elif guess < number:
            print("Higher")
        else:
            print("-------------------------------------------")
            print("Congratulations!")
            print("You won!")
            print("-------------------------------------------")

guess_number()