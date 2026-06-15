"""
Quiz User Interface Module

This module defines the QuizInterface class that creates and manages the GUI for the quiz.
"""

import os
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """
    Manages the graphical user interface for the quiz application using tkinter.
    
    Attributes:
        quiz_brain (QuizBrain): The quiz logic handler.
        window (Tk): The root tkinter window.
        score_label (Label): Displays the current score.
        canvas (Canvas): Canvas widget for displaying questions.
        question_text (int): Canvas object ID for the question text.
        true_img (PhotoImage): Image for the True button.
        false_img (PhotoImage): Image for the False button.
        true_button (Button): Button for True answer.
        false_button (Button): Button for False answer.
    """

    def __init__(self, quiz_brain: QuizBrain) -> None:
        """
        Initialize the QuizInterface with a QuizBrain instance.
        
        Args:
            quiz_brain (QuizBrain): The quiz logic handler instance.
        """
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.create_ui()
        self.get_next_question()
        self.window.mainloop()
    
        
    
    def create_ui(self) -> None:
        """
        Create and configure all UI elements including the canvas, labels, and buttons.
        """
        
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")

        self.question_text = self.canvas.create_text(150,125,width=280,text="Some Question Text",fill=THEME_COLOR,font=("Arial",16,"italic"))

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        # Get the directory of the current file and construct relative paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        true_img_path = os.path.join(current_dir, "images", "true.png")
        false_img_path = os.path.join(current_dir, "images", "false.png")

        self.true_img = PhotoImage(file=true_img_path)
        self.false_img = PhotoImage(file=false_img_path)
        
        self.true_button = Button(image=self.true_img,highlightthickness=0,bg=THEME_COLOR,command=self.true_pressed)

        self.true_button.grid(row=2,column=0)

        self.false_button = Button(image=self.false_img,highlightthickness=0,bg=THEME_COLOR,command=self.false_pressed)

        self.false_button.grid(row=2,column=1)
    
    def get_next_question(self) -> None:
        """
        Display the next question or show the quiz completion message.
        Updates the score label and handles the quiz end state.
        """
        
        self.canvas.config(bg="white")
        
        if self.quiz_brain.still_has_questions():
            
            self.score_label.config(text=f"Score : {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        
        else:          
            self.canvas.itemconfig(self.question_text,text="You have reached of the questions!!")
            print("You've completed the quiz")
            print(f"Your final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    
    def true_pressed(self) -> None:
        """
        Handle the True button press event.
        Checks if the answer is correct and provides feedback.
        """
        
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)
    

def false_pressed(self) -> None:
        """
        Handle the False button press event.
        Checks if the answer is correct and provides feedback.
        """

        is_right = self.quiz_brain.check_answer("False")

        self.give_feedback(is_right)
        

def give_feedback(self, is_right: bool) -> None:
        """
        Provide visual feedback to the user (green for correct, red for wrong).
        Automatically loads the next question after a brief delay.
        
        Args:
            is_right (bool): True if the answer was correct, False otherwise.
        """
           
        if is_right:           
            self.canvas.config(bg="green")
            
        else:
            self.canvas.config(bg="red")
            
        
        self.window.after(1000,self.get_next_question)
    
    

        

    


        


