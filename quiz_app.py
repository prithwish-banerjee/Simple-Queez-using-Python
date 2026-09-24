import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "What is the full form of CSS?",
        "options": ["A) Cascading Style Sheets", "B) Computer Style Sheets", "C) Complete Style Sheets", "D) None of the above"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
        "answer": "C"
    }
]

# Variables
current_question = 0
score = 0

# Function to load question
def load_question():
    question_label.config(
        text=f"Q{current_question + 1}: {questions[current_question]['question']}"
    )

    options = questions[current_question]['options']

    option1.config(text=options[0], value="A")
    option2.config(text=options[1], value="B")
    option3.config(text=options[2], value="C")
    option4.config(text=options[3], value="D")

    selected_option.set(None)

# Function to check answer
def next_question():
    global current_question, score

    user_answer = selected_option.get()

    if user_answer == questions[current_question]['answer']:
        score += 1
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showerror(
            "Result",
            f"Wrong!\nCorrect Answer: {questions[current_question]['answer']}"
        )

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        messagebox.showinfo(
            "Quiz Finished",
            f"Your final score is {score}/{len(questions)}"
        )
        root.destroy()

# GUI Window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("500x350")

# Question Label
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450)
question_label.pack(pady=20)

# Selected Option Variable
selected_option = tk.StringVar()

# Radio Buttons
option1 = tk.Radiobutton(root, text="", variable=selected_option, value="A", font=("Arial", 12))
option1.pack(anchor="w", padx=50)

option2 = tk.Radiobutton(root, text="", variable=selected_option, value="B", font=("Arial", 12))
option2.pack(anchor="w", padx=50)

option3 = tk.Radiobutton(root, text="", variable=selected_option, value="C", font=("Arial", 12))
option3.pack(anchor="w", padx=50)

option4 = tk.Radiobutton(root, text="", variable=selected_option, value="D", font=("Arial", 12))
option4.pack(anchor="w", padx=50)

# Next Button
next_button = tk.Button(root, text="Next", command=next_question, font=("Arial", 12))
next_button.pack(pady=20)

# Load First Question
load_question()

# Run GUI
root.mainloop()