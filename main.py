"""
Quizzler Application

A GUI-based quiz application that fetches random trivia questions from the Open Trivia Database
and presents them to the user through an interactive interface built with tkinter.

The application follows object-oriented principles with separate classes for:
- Question: Represents individual quiz questions
- QuizBrain: Handles quiz logic and score tracking
- QuizInterface: Manages the graphical user interface
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


def main() -> None:
    """
    Initialize and run the quiz application.
    
    Creates a question bank from the fetched question data, initializes the quiz brain,
    and launches the GUI interface.
    """
    # Create Question objects from the question data
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    # Initialize the quiz brain with the question bank
    quiz = QuizBrain(question_bank)

    # Create and display the UI (mainloop runs inside QuizInterface.__init__)
    ui = QuizInterface(quiz)


if __name__ == "__main__":
    main()        


