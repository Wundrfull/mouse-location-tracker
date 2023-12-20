import tkinter as tk
from pynput import mouse, keyboard
import pyperclip

def on_click(x, y, button, pressed):
    global start_x, start_y, regions
    if pressed:
        start_x, start_y = x, y
    else:
        end_x, end_y = x, y
        width, height = end_x - start_x, end_y - start_y
        region_details = f"({start_x}, {start_y}, {width}, {height})"
        regions.append(region_details)
        update_region_history()
        pyperclip.copy(region_details)  # Copy the latest region in the specified format

def update_region_history():
    history_text = '\n'.join(regions)
    label_history.config(text=history_text)

def on_press(key):
    if key == keyboard.Key.esc or (hasattr(key, 'char') and key.char == 'q'):
        stop_listeners()
        root.destroy()

def stop_listeners():
    listener_mouse.stop()
    listener_keyboard.stop()

# Set up the main application window
root = tk.Tk()
root.title("Mouse Region Tracker")

# Set the initial size of the window
root.geometry("600x400")  # Width x Height

# Create a label to display the region history
label_history = tk.Label(root, font=("Helvetica", 12), justify=tk.LEFT)
label_history.grid(row=0, column=0, sticky="w")

# Global variables
start_x, start_y = 0, 0
regions = []  # List to store region details

# Start the mouse position listener
listener_mouse = mouse.Listener(on_click=on_click)
listener_mouse.start()

# Start the keyboard listener
listener_keyboard = keyboard.Listener(on_press=on_press)
listener_keyboard.start()

root.protocol("WM_DELETE_WINDOW", stop_listeners)
root.mainloop()
