Clipboard Reader

This script provides a simple utility that reads aloud the text content from the system clipboard whenever the "q" key is pressed. It utilizes the tkinter library to capture keypress events and espeak for text-to-speech conversion.
Features:

    Read Clipboard: Pressing the "q" key triggers the reading of clipboard contents.
    Text-to-Speech: Uses the espeak command-line utility to convert text into audible speech.
    Tkinter Keypress Listener: A minimalistic tkinter window is used to capture keypress events.

Usage:

    Ensure you have the pyperclip library installed. You can install it via pip:

    pip install pyperclip

    Ensure you have espeak installed on your system. Most Linux distributions come with it pre-installed, but you can also install it manually using your package manager.
    Run the script.
    Copy some text to your clipboard.
    Press the "q" key. The script will read the content of the clipboard aloud.
    Close the tkinter window to terminate the script.

Code Structure:

    speak: This function accepts a text string and uses the espeak command to read it aloud with specified voice parameters.
    read_clipboard: Checks the system clipboard for text content. If text is found, it's read aloud using the speak function.
    on_key_press: Event handler for keypress events. It checks if the pressed key is "q" and triggers the read_clipboard function accordingly.
    root: A simple tkinter window that captures keypress events.

Important Notes:

    The script uses espeak with specific voice and speed parameters. You can modify these parameters in the speak function to adjust the voice output to your preference.
    Ensure that the espeak utility is available on your system PATH to make it accessible by the script.
    The script runs indefinitely and listens for the "q" keypress. To stop the script, close the tkinter window.
