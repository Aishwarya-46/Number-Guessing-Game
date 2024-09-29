import tkinter as tk
import random

class GuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Guessing Game")

        # Set the range of the random number
        self.min_number = 1
        self.max_number = 100

        # Generate a random number within the range
        self.secret_number = random.randint(self.min_number, self.max_number)

        # Set the number of attempts
        self.attempts = 6

        # Create a label to display hints and remaining attempts
        self.hint_label = tk.Label(self.root, text="")
        self.hint_label.pack()

        # Create an entry field for user input
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        # Create a button to submit guesses
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_guess)
        self.submit_button.pack()

        # Start the game loop
        self.root.mainloop()

    def submit_guess(self):
        # Get the user's guess from the entry field
        guess = int(self.guess_entry.get())

        # Check if the guess is correct
        if guess == self.secret_number:
            self.hint_label.config(text="Congratulations! You guessed the correct number!")
            self.submit_button.config(state="disabled")
        elif guess > self.secret_number:
            self.hint_label.config(text="Too high! Try again.")
        else:
            self.hint_label.config(text="Too low! Try again.")

        # Decrease the number of attempts
        self.attempts -= 1

        # Update the label to display remaining attempts
        self.hint_label.config(text=self.hint_label.cget("text") + f" Remaining attempts: {self.attempts}")

        # If the player runs out of attempts, reveal the secret number and disable the button
        if self.attempts == 0:
            self.hint_label.config(text=f"Sorry, you didn't guess the number. The correct answer was {self.secret_number}.")
            self.submit_button.config(state="disabled")

if __name__ == "__main__":
    GuessingGame()