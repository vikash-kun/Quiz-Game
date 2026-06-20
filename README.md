# Quiz-Game

# Python Quiz Game (CLI)

A terminal-based multiple-choice quiz game built in Python to practice Lists, Loops, OOP, Functions, and Recursion.

## Features

- 8 multiple-choice questions on Python/CS basics
- Questions shuffle on every playthrough
- Player object tracks name, score, and answer history
- Recursive countdown (3... 2... 1... GO!) before the quiz starts
- Scorecard with grade (S/A/B/C/D) at the end
- "Play again?" loop - no need to restart the script

## How to Run

```bash
python game.py
```

Make sure you're using Python 3.6+ (for f-strings).

## How to Play

1. Enter your name when prompted.
2. Read each question and pick A, B, C, or D.
3. Get instant feedback (Correct / Wrong) after every answer.
4. View your final scorecard with a grade and a fun recursion-powered fact.
5. Choose to play again (y) or exit (n).


## Project Structure

```
game.py   # single-file CLI app
README.md      # this file
```

## Possible Next Steps

- Add a timer per question
- Save high scores to a file (json)
- Add categories or difficulty levels
- Track wrong answers and show a "review" at the end

## Author

Built by Vikash (vikash-kun) while practicing Python fundamentals.