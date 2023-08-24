import random

rpc = ("rock", "paper", "scissors")
score = 0
i = 1
boolean = True

while boolean:
    try:
        literate = int(input("Enter the number of times to play (1 to 5): "))
        if 1 <= literate <= 5:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while literate > 0:
    computer_choice = random.choice(rpc)
    human_choice = input(f"{i} : Select (rock, paper, scissors): ").lower()
    i += 1
    if human_choice in rpc:
        print("Computer's choice:", computer_choice)

        if human_choice == computer_choice:
            print("nothing")
        elif (
            (human_choice == "rock" and computer_choice == "scissors")
            or (human_choice == "paper" and computer_choice == "rock")
            or (human_choice == "scissors" and computer_choice == "paper")
        ):
            score += 1
            print(f"Score: {score}")
        else:
            score -= 1
            print(f"Score: {score}")

        literate -= 1

if score > 0:
    print("------------------------------------------")
    print("You won!")
    print("------------------------------------------")
elif score < 0:
    print("------------------------------------------")
    print("You lose!")
    print("------------------------------------------")
else:
    print("------------------------------------------")
    print("It's a tie!")
    print("------------------------------------------")
