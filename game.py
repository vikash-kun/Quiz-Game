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
    """prints the game bannerp"""
    print("\n" + "=" * 50)
    print("          PYTHON QUIZ GAME")
    print("=" * 50)
    print("  tpics: OOP , Recursion and Python Basics")
    print("=" * 50 + "\n")
 
 
def display_question(number, total, question_data):
    """displays a single question with options"""

    print(f"\n  question {number}/{total}")


    print(f"  {question_data['question']}\n")

    for option in question_data["options"]:

        print(f"    {option}")
    print()
 
 
def get_user_answer():
    """prompts user for a valid answer (A/B/C/D)"""
    while True:                             
        answer = input("  your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("  Please enter A, B, C, or D")
 
 
def show_result(is_correct, correct_answer):
    """prints feedback after each answer"""
    if is_correct:
        print("Correct!\n")
    else:
        print(f"  wrong! correct answer was: {correct_answer}\n")
    time.sleep(0.8)
 
 
def calculate_grade(score, total):
    """returns a letter grade based on score percentage"""
    percent = (score / total) * 100
    if percent == 100:
        return "S", "perfect score!"
    elif percent >= 75:
        return "A", "excellent work!"
    elif percent >= 50:
        return "B", "good job!"
    elif percent >= 25:
        return "C", "keep practicing!"
    else:
        return "D", "don't give up!"
 

def countdown(n):
    """recursive countdown from n to 1"""
    if n == 0:                                
        print("  GO!\n")
        return
    print(f"  Starting in {n}...")
    time.sleep(0.6)
    countdown(n - 1)                      
 
 
def factorial(n):
    """classic recursion example  computes n!"""
    if n == 0 or n == 1:                     
        return 1
    return n * factorial(n - 1)            
 
 

class Player:
    """represents a quiz player with a name and score"""
 
    def __init__(self, name):
        self.name = name        
        self.score = 0
        self.history = []         
 
    def correct(self):
        """called when player answers correctly"""
        self.score += 1
        self.history.append("correct")
 
    def wrong(self):
        """called when player answers wrong"""
        self.history.append("wrong")
 
    def show_scorecard(self, total):
        """displays final scorecard"""
        grade, message = calculate_grade(self.score, total)
        print("\n" + "=" * 50)
        print(f"   SCORECARD — {self.name}")
        print("=" * 50)
        print(f"  score  : {self.score} / {total}")
        print(f"  grade  : {grade}")
        print(f"  answers: {' '.join(self.history)}")
        print(f"\n  {message}")
 
      
        print(f"\n   fun fact: {self.score}! (factorial) = {factorial(self.score)}")
        print("=" * 50 + "\n")
 
 

 
def run_quiz(player, questions):
    """main quiz loop  iterates over questions list"""
    total = len(questions)
 
    for index, q in enumerate(questions, start=1):   # LOOP with index
        display_question(index, total, q)
        user_answer = get_user_answer()
 
        if user_answer == q["answer"]:
            player.correct()
            show_result(True, q["answer"])
        else:
            player.wrong()
            show_result(False, q["answer"])
 
    player.show_scorecard(total)
 
 
def main():
    display_banner()
 
    
    name = input("  Enter your name: ").strip()
    if not name:
        name = "Player"
 
   
    player = Player(name)
 
  
    selected = random.sample(QUESTIONS, len(QUESTIONS))
 
    print(f"\n  Welcome, {player.name}! Get ready...")
    countdown(3)            
 
    run_quiz(player, selected)
 
   
    while True:
        again = input("  Play again? (y/n): ").strip().lower()
        if again == "y":
            player.score = 0
            player.history = []
            random.shuffle(selected)
            countdown(3)
            run_quiz(player, selected)
        elif again == "n":
            print(f"\n  Thanks for playing, {player.name}! 👋\n")
            break
        else:
            print("  Enter y or n.")
 
 
if __name__ == "__main__":
    main()
 