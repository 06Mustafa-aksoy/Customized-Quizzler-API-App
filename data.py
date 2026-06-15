"""
Quiz Data Module

This module fetches quiz questions from the Open Trivia Database API.
It handles API requests and provides question data for the quiz.
"""

import requests
from typing import List, Dict, Any

# API endpoint for fetching true/false trivia questions
API_URL = "https://opentdb.com/api.php?amount=10&type=boolean"

question_data: List[Dict[str, Any]] = []

try:
    """
    Fetch quiz questions from the Open Trivia Database API.
    
    The API returns 10 random true/false questions with various categories and difficulties.
    Questions are stored in the question_data list for use in the quiz.
    
    If the API request fails, an empty list is used as a fallback.
    """
    response = requests.get(url=API_URL, timeout=5)
    response.raise_for_status()  # Raise exception for bad status codes
    question_data = response.json()["results"]
    
except requests.exceptions.Timeout:
    print("Error: API request timed out. Please check your internet connection.")
    question_data = []
except requests.exceptions.ConnectionError:
    print("Error: Failed to connect to the API. Please check your internet connection.")
    question_data = []
except requests.exceptions.HTTPError as e:
    print(f"Error: HTTP error occurred - {e}")
    question_data = []
except requests.exceptions.RequestException as e:
    print(f"Error: An error occurred while fetching questions - {e}")
    question_data = []
except (KeyError, ValueError) as e:
    print(f"Error: Failed to parse API response - {e}")
    question_data = []






'''
question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The first computer bug was formed by faulty wires.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "AMD created the first consumer 64-bit processor.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "'HTML' stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "hard",
        "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    }
]

'''
