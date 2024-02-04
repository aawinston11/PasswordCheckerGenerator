# Python Password Rater and Generator
## Introduction
This repository contains a Python script that serves two primary functions:

1. Generating random passwords of specified length.
2. Checking the strength of a given password.
Built with a graphical user interface (GUI) using Tkinter, this script offers an easy and interactive way to ensure your passwords are both secure and strong. It also automatically copies generated passwords to the clipboard for convenience while ensuring users are reminded of security best practices when using shared or public computers.

## Features
- Password Strength Checker: Analyzes passwords based on length, the inclusion of lowercase and uppercase letters, numbers, and special characters. It rates passwords as Very Weak, Weak, Moderate, Strong, or Very Strong.
- Random Password Generator: Creates a secure, random password based on the user-specified length. The generated password includes a mix of letters, numbers, and special characters.
- Clipboard Integration: Automatically copies generated passwords to the clipboard for easy use.
- Security Notice: Provides a reminder to clear the clipboard after using the generated password, enhancing security on shared or public computers.
## Prerequisites
Before running the script, ensure you have the following installed:

- Python 3.x
- Tkinter (usually included with Python)
- Pyperclip
## Installation
1. Clone this repository to your local machine.

2. Install Pyperclip using pip if you haven't already:
    - pip install pyperclip
## Usage
To run the script, navigate to the directory containing the script and run:

python password_tool.py

A GUI window will open with two main functionalities:

- Check Password Strength: Enter a password to check its strength.
- Generate Password: Click to generate a random password. You will be prompted to enter the desired length of the password.
## Contributing
Contributions to the Python Password Rater and Generator are welcome! Please read through the contributing guidelines before making any changes or suggestions.
