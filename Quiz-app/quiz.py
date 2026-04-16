import tkinter as tk
from tkinter import messagebox

# ____________Questions___________________________
questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pt", ".py", ".pyt", ".python"],
        "answer": ".py"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "What will print(2 ** 3) output?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which of the following is a Python list?",
        "options": ["{1,2,3}", "(1,2,3)", "[1,2,3]", "<1,2,3>"],
        "answer": "[1,2,3]"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },
    {
        "question": "What is the output of print(type(5))?",
        "options": ["int", "<class 'int'>", "integer", "type int"],
        "answer": "<class 'int'>"
    },
]


# _____________________App Class_____________________
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.config(bg="white")   # WHITE BACKGROUND

        self.q_index = 0
        self.score = 0

        # Heading
        self.title = tk.Label(
            root,
            text="Quiz Game",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="black"
        )
        self.title.pack(pady=20)

        # Question label
        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 16),
            wraplength=400,
            bg="white",
            fg="black"
        )
        self.question_label.pack(pady=20)

        # Buttons
        self.buttons = []
        for i in range(4):
            btn = tk.Button(
                root,
                text="",
                width=25,
                height=2,
                bg="#3498db",
                fg="white",
                font=("Arial", 12),
                activebackground="#2980b9",
                command=lambda i=i: self.check_answer(i)
            )
            btn.pack(pady=8)
            self.buttons.append(btn)

        self.load_question()


# ____________Load Question___________________
    def load_question(self):
        q = questions[self.q_index]

        self.question_label.config(text=q["question"])

        for i in range(4):
            self.buttons[i].config(
                text=q["options"][i],
                bg="#3498db",
                fg="white",
                state="normal"
            )


# ________________Check Answer___________________________
    def check_answer(self, i):
        selected = self.buttons[i].cget("text")
        correct = questions[self.q_index]["answer"]

        # disable all buttons
        for btn in self.buttons:
            btn.config(state="disabled")

        # reset text color for clicked button + feedback colors
        if selected == correct:
            self.buttons[i].config(bg="green", fg="black")
            self.score += 1
        else:
            self.buttons[i].config(bg="red", fg="black")

        self.q_index += 1

        if self.q_index < len(questions):
            self.root.after(1000, self.load_question)
        else:
            self.root.after(
                1000,
                lambda: messagebox.showinfo(
                    "Result",
                    f"Your Score : {self.score}/ {len(questions)}"
                )
            )
            self.root.after(1200, self.root.quit)


# _____________Run App__________
root = tk.Tk()
app = QuizApp(root)
root.mainloop()