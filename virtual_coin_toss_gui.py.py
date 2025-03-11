import tkinter as tk
import random

# Function to simulate coin toss
def flip_coin():
    result = random.choice(["Heads", "Tails"])
    result_label.config(text=f"Result: {result}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Virtual Coin Toss")
root.geometry("300x200")

# Label to display the result
result_label = tk.Label(root, text="Click to Flip the Coin!", font=("Arial", 14))
result_label.pack(pady=20)

# Button to flip the coin
flip_button = tk.Button(root, text="Flip Coin", command=flip_coin, font=("Arial", 12))
flip_button.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), fg="white", bg="red")
exit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
