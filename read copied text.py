import tkinter as tk
import pyperclip
import subprocess
import time

def speak(text):
    # use espeak command to read text aloud with specified voice and parameters
    subprocess.call(["espeak", "-s", "150", "-v", "en-us-mbrola-1", "-p", "40", "-k", "5", "-s", "140", text])

def read_clipboard():
    # get text from clipboard
    clipboard_text = pyperclip.paste()
    
    # check if clipboard has text
    if clipboard_text.strip() != "":
        speak(clipboard_text)
    else:
        print("Clipboard is empty")
    
    # wait for a moment to prevent accidental repeat
    time.sleep(0.5)

def on_key_press(event):
    # check if the key pressed is "q" or "Q"
    if event.char.lower() == "q":
        read_clipboard()

# create a tkinter window to capture keystrokes
root = tk.Tk()
root.bind("<Key>", on_key_press)
root.mainloop()
