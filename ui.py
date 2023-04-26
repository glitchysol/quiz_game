from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=300, height=500, bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Quiz info",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.score_count = Label(text=f"Score: 0", font=("Arial", 14, "normal"), bg=THEME_COLOR, fg="white")
        self.score_count.grid(row=0, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_count.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
            # self.canvas.config(bg="white")
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
            # self.canvas.config(bg="white")


