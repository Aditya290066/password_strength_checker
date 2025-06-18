import tkinter as tk
import re
import nltk
from nltk.corpus import words
import random
import string

nltk.download('words')

def toggle_password_visibility():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        eye_button.config(text='⏼')  # Power ON (visible)
    else:
        password_entry.config(show='*')
        eye_button.config(text='⏻')  # Power OFF (hidden)

def analyze_password(password):
    strength = "Weak"
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    else:
        strength = "Medium"

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters.")
    if not re.search(r"[0-9]", password):
        suggestions.append("Add numbers.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Add at least one special character.")

    if password.lower() in words.words():
        suggestions.append("Avoid dictionary words.")

    if len(suggestions) == 0 and len(password) >= 12:
        strength = "Strong"

    return strength, "\n".join(suggestions) if suggestions else "Good password!"

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(15))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def check_password():
    password = password_entry.get()
    strength, suggestions = analyze_password(password)
    color = {"Weak": "red", "Medium": "blue", "Strong": "green"}.get(strength, "black")
    feedback_label.config(text=f"Strength: {strength}\nTips: {suggestions}", fg=color, font=("Arial", 12))

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

label = tk.Label(main_frame, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

entry_frame = tk.Frame(main_frame)
entry_frame.pack()

password_entry = tk.Entry(entry_frame, show="*", font=("Arial", 12), width=25)
password_entry.pack(side=tk.LEFT)

eye_button = tk.Button(entry_frame, text="⏻", command=toggle_password_visibility, 
                      relief=tk.FLAT, font=("Arial", 12))
eye_button.pack(side=tk.LEFT)

button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

check_button = tk.Button(button_frame, text="Check It!", command=check_password, font=("Arial", 10))
check_button.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password, font=("Arial", 10))
generate_button.pack(side=tk.LEFT, padx=5)

feedback_label = tk.Label(main_frame, text="", font=("Arial", 12), wraplength=350)
feedback_label.pack(pady=20)


root.mainloop()
