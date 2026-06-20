import random
import time

QUESTIONS = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Core Processing Utility"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["A. 6", "B. 9", "C. 8", "D. 5"],
        "answer": "C"
    },
    {
        "question": "Which data structure uses LIFO order?",
        "options": ["A. Queue", "B. Stack", "C. List", "D. Tree"],
        "answer": "B"
    },
    {
        "question": "What does OOP stand for?",
        "options": ["A. Object Oriented Program", "B. Output-Oriented Programming", "C. Object-Oriented Programming", "D. Open Object Protocol"],
        "answer": "C"
    },
    {
        "question": "Which of these is a mutable data type in Python?",
        "options": ["A. tuple", "B. str", "C. int", "D. list"],
        "answer": "D"
    },
    {
        "question": "What is recursion?",
        "options": ["A. A loop that never ends", "B. A function that calls itself", "C. A type of class", "D. A sorting algorithm"],
        "answer": "B"
    },
    {
        "question": "Which Python keyword is used for inheritance?",
        "options": ["A. extends", "B. inherits", "C. super", "D. class ChildClass(ParentClass)"],
        "answer": "D"
    },
]

def display_banner():
    """Prints the game banner."""
    print("\n" + "=" * 50)
    print("        🎯  PYTHON QUIZ GAME")
    print("=" * 50)
    print("  Topics: OOP | Recursion | Python Basics")
    print("=" * 50 + "\n")
 
 
def display_question(number, total, question_data):
    """Displays a single question with options."""

    print(f"\n  Question {number}/{total}")


    print(f"  {question_data['question']}\n")

    for option in question_data["options"]:

        print(f"    {option}")
    print()
 
 
def get_user_answer():
    """Prompts user for a valid answer (A/B/C/D)."""
    while True:                             
        answer = input("  Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("  Please enter A, B, C, or D")
 
 
def show_result(is_correct, correct_answer):
    """Prints feedback after each answer."""
    if is_correct:
        print("Correct!\n")
    else:
        print(f"  Wrong! Correct answer was: {correct_answer}\n")
    time.sleep(0.8)
 
 
def calculate_grade(score, total):
    """Returns a letter grade based on score percentage."""
    percent = (score / total) * 100
    if percent == 100:
        return "S", "Perfect score!"
    elif percent >= 75:
        return "A", "Excellent work!"
    elif percent >= 50:
        return "B", "Good job!"
    elif percent >= 25:
        return "C", "Keep practicing!"
    else:
        return "D", "Don't give up!"
 