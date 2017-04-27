#!/usr/bin/python3

from tkinter import *

window = Tk()
window.geometry("500x500")

window_message_text = StringVar()
window_message = Message(window, textvariable = window_message_text)
window_message_text.set("FILL IN THE BLANK\n_ _ _ _ _    _ _ _ _ _")
window_message.config(width=500, pady=100, font=("Consolas", 40),
	bg = 'light blue')
window_message.pack()

### NEW ###
## CREATE ENTRY
## Notable entry attributes:
# bg:		Background color of entry
# textvariable:	Contains the inputted text
# font:		Font of text
window_entry_text = StringVar()
# Set Default Text
window_entry_text.set("SHMELLO SHMORLD")

window_entry = Entry(window, bg = "white",
	width = 500,
	textvariable = window_entry_text)
window_entry.pack()

## CREATE BUTTON
## Notable button attributes:
# bg:		Background color of button
# command:	Function called when button
#			is clicked
# state:	DISABLED/NORMAL/ACTIVE,
#			determines if button is
#			clickable
def check_answer():
	if(window_entry_text.get() == "HELLO WORLD"):
		window_message_text.set("YOU DID IT!")
	else:
		window_message_text.set("FILL IN THE BLANK\n_____ _____")

window_button_text = StringVar()
window_button_text.set("SUBMIT")

window_button = Button(window,
	textvariable = window_button_text,
	command = check_answer)
window_button.pack()
### NEW ###

window.mainloop()

exit()