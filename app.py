import tkinter as tk
from tkinter import ttk
import serial

# Connect to the Arduino board
arduino = serial.Serial('COM5', 9600)  # Replace with the correct port and baud rate

# Create the main window
root = tk.Tk()
root.title("OBot v1")

# Create the main frame
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Create the control buttons
forward_button = ttk.Button(main_frame, text="Forward", command=lambda: send_command("forward"))
forward_button.grid(row=0, column=1, padx=10, pady=10)

backward_button = ttk.Button(main_frame, text="Backward", command=lambda: send_command("backward"))
backward_button.grid(row=2, column=1, padx=10, pady=10)

left_button = ttk.Button(main_frame, text="Left", command=lambda: send_command("left"))
left_button.grid(row=1, column=0, padx=10, pady=10)

right_button = ttk.Button(main_frame, text="Right", command=lambda: send_command("right"))
right_button.grid(row=1, column=2, padx=10, pady=10)

stop_button = ttk.Button(main_frame, text="Stop", command=lambda: send_command("stop"))
stop_button.grid(row=1, column=1, padx=10, pady=10)

# Function to send commands to the Arduino
def send_command(command):
    arduino.write(command.encode())

# Run the main event loop
root.mainloop()