import os
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.create_ui()
        self.get_next_question()
        self.window.mainloop()
    
    def create_ui(self) -> None:
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        true_img_path = os.path.join(current_dir, "images", "true.png")
        false_img_path = os.path.join(current_dir, "images", "false.png")

        self.true_img = PhotoImage(file=true_img_path)
        self.false_img = PhotoImage(file=false_img_path)
        
        self.true_button = Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
    
    def get_next_question(self) -> None:
        self.canvas.config(bg="white")
        
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:          
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the questions!!")
            print("You've completed the quiz")
            print(f"Your final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self) -> None:
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self) -> None:
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right: bool) -> None:
        if is_right:           
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)
    
    

        

    


        


