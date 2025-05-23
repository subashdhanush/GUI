import tkinter as tk
from tkinter import messagebox
import json

# Load questions
with open("questions.json", "r") as file:
    questions = json.load(file)

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Buzz - GUI")
        self.master.geometry("500x400")
        self.qn_index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 16), wraplength=450)
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(master, text="", font=("Arial", 14), width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.load_question()

    def load_question(self):
        if self.qn_index < len(questions):
            current_q = questions[self.qn_index]
            self.question_label.config(text=current_q["question"])
            for i, option in enumerate(current_q["options"]):
                self.buttons[i].config(text=option)
        else:
            self.show_score()

    def check_answer(self, i):
        selected = self.buttons[i].cget("text")
        correct = questions[self.qn_index]["answer"]
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct!", "✅ Well done!")
        else:
            messagebox.showerror("Wrong!", f"❌ Correct answer: {correct}")
        self.qn_index += 1
        self.load_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score} / {len(questions)}")
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
