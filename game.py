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