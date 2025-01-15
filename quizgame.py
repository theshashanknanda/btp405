question_answers = {
    "Question one? " : "A",
    "Question two? " : "B",
    "Question three? " : "C",
    "Question four? " : "D"
}

options = [
    ["Q1. Option 1", "Q1. Option 2", "Q1. Option 3", "Q1. Option 4"],
    ["Q2. Option 1", "Q2. Option 2", "Q2. Option 3", "Q2. Option 4"],
    ["Q3. Option 1", "Q3. Option 2", "Q3. Option 3", "Q3. Option 4"],
    ["Q4. Option 1", "Q4. Option 2", "Q4. Option 3", "Q4. Option 4"]
]

def start_game():
    question_num = 1
    for q, a in question_answers.items():
        print(q)
        for option in options[question_num - 1]:
            print(option)
        question_num += 1

        guess = input('Enter your guess: ')
        if guess == a:
            print("Correct!")
        else:
            print('Incorrect!')
        print()

start_game()
