import tkinter as tk
from pynput import mouse, keyboard
import pyperclip

def on_move(x, y):
    global current_position
    current_position = f"X: {x}, Y: {y}"
    label.config(text=current_position)

def on_press(key):
    if key == keyboard.Key.esc or (hasattr(key, 'char') and key.char == 'q'):
        pyperclip.copy(current_position)
        listener_mouse.stop()
        listener_keyboard.stop()
        root.destroy()

# Set up the main application window
root = tk.Tk()
root.title("Mouse Position Tracker")

# Create a label to display the mouse coordinates
label = tk.Label(root, font=("Helvetica", 16))
label.pack()

# Global variable to hold the current position
current_position = ""

# Start the mouse position listener
listener_mouse = mouse.Listener(on_move=on_move)
listener_mouse.start()

# Start the keyboard listener
listener_keyboard = keyboard.Listener(on_press=on_press)
listener_keyboard.start()

# Run the application
root.mainloop()
