from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.config(padx=30, bg=THEME_COLOR)

        # Create and configure canvas for question display
        self.canvas = Canvas(width=300, height=300, bg="white")
        self.question_text = self.canvas.create_text(150, 150, text="Question", font=("Arial", 20, "bold"),
                                                     width=250, fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Create and configure label for score display
        self.score = Label(text="Score: 0/0", pady=20, bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score.grid(row=0, column=0, columnspan=2)

        # Create and configure true button
        self.true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_button_image, command=self.right_button_clicked)
        self.true_button.config(highlightthickness=0)
        self.true_button.grid(row=2, column=0, pady=20, padx=(0, 10))

        # Create and configure false button
        self.false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_button_image, command=self.wrong_button_clicked)
        self.false_button.config(highlightthickness=0)
        self.false_button.grid(row=2, column=1, pady=20, padx=(10, 0))

        self.update_question()
        self.update_score()

        self.window.mainloop()

    def update_question(self):
        self.canvas.itemconfigure(self.question_text, text=self.quiz.next_question())

    def right_button_clicked(self):
        self.check_answer_and_update("True")

    def wrong_button_clicked(self):
        self.check_answer_and_update("False")

    def check_answer_and_update(self, answer):
        if self.quiz.still_has_questions():
            self.quiz.check_answer(answer)
            self.update_score()
            self.update_question()
        else:
            self.quiz_ends()

    def update_score(self):
        self.score.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")

    def quiz_ends(self):
        self.canvas.itemconfigure(self.question_text, text="END")


if __name__ == "__main__":
    quiz = QuizBrain()  # Create an instance of QuizBrain class
    quiz_ui = QuizUI(quiz)  # Create an instance of QuizUI class with the quiz instance as an argument
