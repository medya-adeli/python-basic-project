id = 1
questions = (
    "Where is Kurdistan?",
    "Who created me?",
    "Who is Oppenheimer?",
    "Where is Arbaba?",
    "Who invented the computer?"
)

options = (
    ('A. Pakistan', 'B. Iran', 'C. Syria', 'D. Heart'),
    ('A. graph', 'B. namo', 'C. zhiuxer', 'D. Kia'),
    ('A. Artist', 'B. Actor', 'C. Physicist', 'D. Prophet'),
    ('A. Bane', 'B. Mahabad', 'C. Piranshahr', 'D. Saqez'),
    ('A. albert', 'B. mohammed', 'C. mosa', 'D. Alan Turing')
)

answers = ('D', 'B', 'C', 'A', 'D')
guesses = []
score = 0

for i, question in enumerate(questions):
    int("-------------------------")
    int(f"Question {i+1}: {question}")
    for option in options[i]:
        int(option)

    while True:
        answer = input("Your answer (enter A, B, C, or D): ").upper()
        if answer in ('A', 'B', 'C', 'D'):
            break
        else:
            int("Invalid input. Please enter A, B, C, or D.")

    guesses.append(answer)

# Scoring
for i in range(len(answers)):
    if guesses[i] == answers[i]:
        score += 1

int("-------------------------")
int("Quiz Results:")
int(f"Total Questions: {len(questions)}")
int(f"Correct Answers: {score}")
int(f"Your Score: {score}/{len(questions)}")
