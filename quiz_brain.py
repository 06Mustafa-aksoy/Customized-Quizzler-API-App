"""
Quiz Brain Module

This module defines the QuizBrain class that handles quiz logic and scoring.
"""

import html
from typing import List
from question_model import Question


class QuizBrain:
    """
    Manages quiz logic including question progression and score tracking.
    
    Attributes:
        question_number (int): Current question number (0-indexed).
        score (int): Current player's score.
        question_list (List[Question]): List of all questions in the quiz.
        current_question (Question): The current question being asked.
    """

    def __init__(self, q_list: List[Question]) -> None:
        """
        Initialize the QuizBrain with a list of questions.
        
        Args:
            q_list (List[Question]): List of Question objects for the quiz.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """
        Check if there are more questions remaining in the quiz.
        
        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """
        Get the next question and increment the question counter.
        
        Returns:
            str: Formatted question text with question number.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        
    def check_answer(self, user_answer: str) -> bool:
        """
        Check if the user's answer is correct and update the score.
        
        Args:
            user_answer (str): The answer provided by the user.
            
        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True          
        else:
            return False
        
    
