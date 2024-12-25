import random
import tkinter as tk
from tkinter import messagebox, ttk

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.master.geometry("450x300")
        self.master.configure(bg="#2c3e50")

        self.style = ttk.Style()
        self.style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Helvetica", 12))
        self.style.configure("TButton", background="#2ecc71", foreground="#000000", font=("Helvetica", 12))  # زر التخمين بلون خط أسود
        self.style.map("TButton", background=[("active", "#27ae60")])  # لون عند الضغط

        self.style.configure("Reset.TButton", background="#e74c3c", foreground="#ffffff", font=("Helvetica", 12))  # زر إعادة اللعب
        self.style.map("Reset.TButton", background=[("active", "#c0392b")])  # لون عند الضغط

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10


        self.title_label = ttk.Label(master, text="Guess the Number Game", font=("Helvetica", 16))
        self.title_label.pack(pady=10)


        self.instruction_label = ttk.Label(master, text="I'm thinking of a number between 1 and 100.")
        self.instruction_label.pack(pady=10)


        self.guess_entry = ttk.Entry(master, font=("Helvetica", 14))
        self.guess_entry.pack(pady=10)


        self.guess_button = ttk.Button(master, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.reset_button = ttk.Button(master, text="Play Again", command=self.reset_game, style="Reset.TButton")
        self.reset_button.pack(pady=5)
        self.reset_button.config(state=tk.DISABLED)

        self.footer_label = ttk.Label(master, text="Made with ❤️ by Eng Mustafa")
        self.footer_label.pack(side="bottom", pady=10)


        self.attempts_label = ttk.Label(master, text=f"Attempts Left: {self.max_attempts}")
        self.attempts_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                messagebox.showinfo("Invalid Guess", "Please guess a number between 1 and 100.")
            elif guess < self.number_to_guess:
                messagebox.showinfo("Guess Result", "Higher! Try again.")
                self.update_attempts()
            elif guess > self.number_to_guess:
                messagebox.showinfo("Guess Result", "Lower! Try again.")
                self.update_attempts()
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the number {self.number_to_guess} in {self.attempts} attempts.")
                self.reset_button.config(state=tk.NORMAL)

            if self.attempts >= self.max_attempts and guess != self.number_to_guess:
                messagebox.showinfo("Game Over", f"Sorry, you've used all your attempts. The correct number was {self.number_to_guess}.")
                self.reset_button.config(state=tk.NORMAL)

        except ValueError:
            messagebox.showinfo("Input Error", "Please enter a valid number.")

    def update_attempts(self):
        attempts_left = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts Left: {attempts_left}")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.reset_button.config(state=tk.DISABLED)
        self.attempts_label.config(text=f"Attempts Left: {self.max_attempts}")

        messagebox.showinfo("Game Reset", "The game has been reset. Start guessing!")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()