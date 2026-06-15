"""
Question Model Module

This module defines the Question class that represents a single quiz question.
"""


class Question:
    """
    Represents a single quiz question with its text and correct answer.
    
    Attributes:
        text (str): The question text.
        answer (str): The correct answer to the question.
    """

    def __init__(self, q_text: str, q_answer: str) -> None:
        """
        Initialize a Question object.
        
        Args:
            q_text (str): The question text.
            q_answer (str): The correct answer to the question.
        """
        self.text = q_text
        self.answer = q_answer
