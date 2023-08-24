name_student = input("Enter the name of the student: ")

def get_valid_score(subject_name):
    while True:
        try:
            score = float(input(f"Enter the score for {subject_name} (between 1 and 20): "))
            if 1 <= score <= 20:
                return score
            else:
                int("Invalid input! Score should be between 1 and 20.")
        except ValueError:
            int("Invalid input! Please enter a valid number.")

literature = get_valid_score("Literature")
language = get_valid_score("Language")
art = get_valid_score("Art")
mathematics = get_valid_score("Mathematics")
history = get_valid_score("History")

report_card = (literature + language + art + mathematics + history) / 5
emojis = {
    "excellent": "🏆",
    "good": "👍",
    "average": "😊",
    "below average": "😕",
    "needs improvement": "👎"
}

if report_card >= 18 and report_card <= 20:
    performance_emojis = emojis["excellent"]
elif report_card >= 15 and report_card <= 17:
    performance_emojis = emojis["good"]
elif report_card >= 12 and report_card <= 14:
    performance_emojis = emojis["average"]
elif report_card >= 9 and report_card <= 11:
    performance_emojis = emojis["below average"]
elif report_card >= 6 and report_card <= 8:
    performance_emojis = emojis["needs improvement"]

int(f"Score of Literature: |{literature}|, Score of Language: |{language}|, Score of Art: |{art}|, Score of Mathematics: |{mathematics}|, Score of History: |{history}|")
int("-----------------------------------------------")
int(f"Report Card for {name_student}: {report_card} {performance_emojis}")
