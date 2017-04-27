#!/usr/bin/python3

from tkinter import *

# Create the main tkinter window
window = Tk()

### NEW ###

# Set window size with X px by Y px
window.geometry("500x500")

### NEW ###

# Create a var that will contain the display text
text = StringVar()
# Create a Message object within our Window
window_message = Message(window, textvariable = text)
# Set the display text
text.set("HELLO WORLD")
# Compile the message with the display text

### NEW ###

## Notable .config Attributes:
# anchor: 	Orientation of text
# bg:		Background color
# font:		Font of text
# width:	Width of text frame
# padx:		Padding on left and right
# pady:		Padding on top and bottom
# and more!

window_message.config(width=500, pady=250, font=("Consolas", 60),
	bg = 'light blue')

### NEW ###

window_message.pack()

# Start the window loop
window.mainloop()

exit()