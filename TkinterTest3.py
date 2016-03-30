from tkinter import *

master = Tk()
master.geometry('952x952')
frame = Frame(master, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

text = Text(frame, wrap=NONE, bd=0, yscrollcommand=yscrollbar.set)
text.insert(INSERT, "Dude \nDude \nDudette \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude \nDude")
text.config(state=DISABLED)
text.grid(row=0, column=0, sticky=N+S+E+W)

yscrollbar.config(command=text.yview)

frame.pack()
