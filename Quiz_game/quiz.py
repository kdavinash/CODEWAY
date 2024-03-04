class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

questions = [
    Question("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], "Paris"),
    Question("What is the largest planet in our solar system?", ["Jupiter", "Venus", "Earth", "Mars"], "Jupiter"),
    Question("Fill in the blank: The Great Wall of China is the longest man-made ________ on Earth.", ["structure", "building", "wall", "road"], "wall"),
]

def display_welcome():
    print("Welcome to the Quiz Game!")
    print("Test your knowledge on various topics.")
    print("You will be presented with multiple-choice and fill-in-the-blank questions.")
    print("Good luck!")

def present_questions(questions):
    score = 0
    for question in questions:
        print(question.question)
        if len(question.choices) > 0:  
            for i, choice in enumerate(question.choices):
                print(f"{i+1}. {choice}")
            user_answer = input("Enter your choice (number): ")
            if int(user_answer) - 1 == question.choices.index(question.answer):
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
                print(f"The correct answer is: {question.answer}")
        else: 
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == question.answer.lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
                print(f"The correct answer is: {question.answer}")
    return score

def display_results(score, total_questions):
    print(f"\nYour final score is: {score}/{total_questions}")
    if score == total_questions:
        print("Congratulations! You answered all questions correctly.")
    else:
        print("Thanks for playing! Try again to improve your score.")

display_welcome()
total_score = present_questions(questions)
display_results(total_score, len(questions))

play_again = input("\nDo you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    present_questions(questions)
    display_results(total_score, len(questions))
else:
    print("Thank you for playing!")
