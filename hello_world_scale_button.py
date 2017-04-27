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

slider = Scale(window,
	    variable = value,
	    orient = HORIZONTAL,
	    showvalue = 0)
slider.pack()

## Create Button
def change_text():
    window_message_text.set("The value was " + str(value.get()))

window_button_text = StringVar()
window_button_text.set("Click")

window_button = Button(window,
		       textvariable = window_button_text,
		       command=change_text)
window_button.pack()

window.mainloop()

exit()
