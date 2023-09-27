# Python Quiz Game
# Store all the questions in a tuple
questions = ("How may planets are in the universe? ",
             "what is the national animal of india? ",
             "What is the chemical symbol of gold? ",
             "How may bones are in the human body? ",
             "Which planet in our solar system is the largest? ")

options = (("A. 6", "B. 8", "C. 10", "D. 9"),
           ("A. Tiger", "B. Horse", "C. Elephant", "D. Lion"),
           ("A. Au", "B. Ag", "C. Fe", "D. Hg"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Jupiter", "C. Earth", "D. Mars"))

answers = ("B", "A", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------------")
print("          Results           ")
print("----------------------------")

print("Correct answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

