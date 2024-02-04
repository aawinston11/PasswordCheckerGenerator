import tkinter as tk
from tkinter import simpledialog, messagebox
import re
import random
import string
import pyperclip

#function to check password strength
def check_password_strength(password):
    strength_points = 0
    #add points based on meeting criteria
    if len(password) >= 8: strength_points += 1
    if len(password) >= 12: strength_points += 1
    if re.search("[a-z]", password): strength_points += 1
    if re.search("[A-Z]", password): strength_points += 1
    if re.search("[0-9]", password): strength_points += 1
    if re.search("[@$#_/?!()]", password): strength_points += 1 #included space as a character

    #return strength based on total strength points
    if strength_points <= 1: return "Very Weak"
    elif strength_points == 2: return "Weak"
    elif strength_points == 3: return "Moderate"
    elif strength_points == 4: return "Strong"
    else: return "Very Strong"

#function to generate a random password
def generate_password(length):
    #Makes 8 the minimum length of password
    if length < 8: length = 8 
    #inludes all possible characters including space
    characters = string.ascii_letters + string.digits + "_@$#/?!()"
    #generate random password
    password = ''.join(random.choice(characters) for each in range(length))
    pyperclip.copy(password) #copy password to clipboard
    return password

#function to update strength label in GUI
def update_strength_label():
    password = password_entry.get()
    strength = check_password_strength(password)
    strength_result_label.config(text=f"Strength: {strength}")

#function for password generation and security message
def update_generated_password():
    length = simpledialog.askinteger("length", "Enter the desired length of the password:", minvalue=8, maxvalue=64)
    if length:
        new_password = generate_password(length)
        generated_password_label.config(text="Generated (copied to clipboard)")
        #Security Message about clipboard data
        messagebox.showinfo("Security Notice",
                            "Password copied to clipboard.\n\nRemember to clear your clipboard after pasting, especially when using shared or public computers.")
        
#Setting up GUI
window = tk.Tk()
window.title("Password Rater and Generator")

#Create Widgets for Password Strength Checker
password_label = tk.Label(window, text="Enter password:")
password_label.pack()

password_entry = tk.Entry(window)
password_entry.pack()

check_button = tk.Button(window, text="Check Strength", command=update_strength_label)
check_button.pack()

strength_result_label = tk.Label(window, text="Strength:")
strength_result_label.pack()

# Create Widgets for Password Generator
generate_button = tk.Button(window, text="Generate Password", command=update_generated_password)
generate_button.pack()

generated_password_label = tk.Label(window, text="Generated:")
generated_password_label.pack()

#Start event loop
window.mainloop()