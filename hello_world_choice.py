#!/usr/bin/python3

from tkinter import *

window = Tk()
window.geometry("500x500")

window_message_text = StringVar()
window_message = Message(window, textvariable = window_message_text)
window_message_text.set("CHOOSE YOUR ADVENTURE")
window_message.config(width = 500, font=("Consolas", 20),
	bg = 'light blue')
window_message.pack()

### NEW ###

## Create Paned Window

## Create Checkbuttons
# Int variables store state of checkbutton
# 0 for unchecked, 1 for checked
check_hello_int = IntVar()
check_greetings_int = IntVar()
check_hola_int = IntVar()

check_hello = Checkbutton(window, text="HELLO",
	variable = check_hello_int, offvalue = 0,
	onvalue = 1)
check_greetings = Checkbutton(window,text="GREETINGS",
	variable = check_greetings_int, offvalue = 0,
	onvalue = 1)
check_hola = Checkbutton(window, text="HOLA",
	variable = check_hola_int, offvalue = 0,
	onvalue = 1)

check_hello.pack()
check_greetings.pack()
check_hola.pack()

## Create Radiobuttons
radio_int = IntVar()

radio_world = Radiobutton(window, text="WORLD",
	variable = radio_int, value = 1)
radio_earth = Radiobutton(window, text="EARTH",
	variable = radio_int, value = 2)
radio_mundo = Radiobutton(window, text="MUNDO",
	variable = radio_int, value = 3)

radio_world.pack()
radio_earth.pack()
radio_mundo.pack()


def submit():
	phrase = ""
	target = ""
	if(check_hello_int.get() == 1):
		phrase = phrase + "HELLO "
	if(check_greetings_int.get() == 1):
		phrase = phrase + "GREETINGS "
	if(check_hola_int.get() == 1):
		phrase = phrase + "HOLA "

	if(radio_int.get() == 1):
		target = "WORLD"
	if(radio_int.get() == 2):
		target = "EARTH"
	if(radio_int.get() == 3):
		target = "MUNDO"
	print(str(phrase + target))
	window_message_text.set(str(phrase + target))

window_button_text = StringVar()
window_button_text.set("SUBMIT")

window_button = Button(window,
	textvariable = window_button_text,
	command = submit)
window_button.pack()
### NEW ###

window.mainloop()

exit()