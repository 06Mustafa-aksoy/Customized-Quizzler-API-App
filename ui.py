THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:

    def __init__(self,quiz_brain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.create_ui()
        self.get_next_question()
        self.window.mainloop()
    
        
    
    def create_ui(self):
        
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")

        self.question_text = self.canvas.create_text(150,125,width=280,text="Some Question Text",fill=THEME_COLOR,font=("Arial",16,"italic"))

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.true_img = PhotoImage(file= "C:/Users/musta/Desktop/Python Training/Day 34/quizzler-app-start/images/true.png")

        self.false_img = PhotoImage(file= "C:/Users/musta/Desktop/Python Training/Day 34/quizzler-app-start/images/false.png")
        
        self.true_button = Button(image=self.true_img,highlightthickness=0,bg=THEME_COLOR,command=self.true_pressed)

        self.true_button.grid(row=2,column=0)

        self.false_button = Button(image=self.false_img,highlightthickness=0,bg=THEME_COLOR,command=self.false_pressed)

        self.false_button.grid(row=2,column=1)
    
    def get_next_question(self):
        
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

    
    def true_pressed(self):
        
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)
    

    def false_pressed(self):

        is_right = self.quiz_brain.check_answer("False")

        self.give_feedback(is_right)
        

    def give_feedback(self,is_right):
           
        if is_right:           
            self.canvas.config(bg="green")
            
        else:
            self.canvas.config(bg="red")
            
        
        self.window.after(1000,self.get_next_question)
    
    

        

    


        


