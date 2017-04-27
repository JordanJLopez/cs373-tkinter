#!/usr/bin/python3

from tkinter import *

window = Tk()
window.geometry("500x500")

window_message_text = StringVar()
window_message = Message(window, textvariable = window_message_text)
window_message_text.set("MOVE THE SLIDER")
window_message.config(width = 500, font=("Consolas", 20),
	bg = 'light blue')
window_message.pack()

### NEW ###

## Create Slider
value = DoubleVar()

def change_text(event=None):
    window_message_text.set("HELLO WORLD " + str(value.get()))
    
slider = Scale(window,
	    variable = value,
	    command = change_text,
	    orient = HORIZONTAL,
	    showvalue = 0)
slider.pack()

window.mainloop()

exit()
