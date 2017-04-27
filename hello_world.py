#!/usr/bin/python3

from tkinter import *

# Create the main tkinter window
window = Tk()

# Create a var that will contain the display text
text = StringVar()
# Create a Message object within our Window
window_message = Message(window, textvariable = text)
# Set the display text
text.set("HELLO WORLD")
# Compile the message with the display text
window_message.pack()

# Start the window loop
window.mainloop()

exit()