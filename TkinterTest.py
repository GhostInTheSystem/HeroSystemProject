from tkinter import *

master = Tk()
master.geometry('1000x1000')

w = Canvas(master, width=5, height=1000)

def pageSwitch(newPage):
    testText.delete(1.0, END)
    testText.insert(INSERT, newPage)

w.grid(row=0, column=56, rowspan=1000)
w.create_line(5, 0, 5, 1000, fill="#000000", width=5)


charDetailsButton = Button(master, text="Character Details", width=20, height=2, command=lambda: pageSwitch("Character Details"))
charDetailsButton.grid(row=0, column=1, rowspan=142, columnspan=55, padx=(25,10))

characteristicButton = Button(master, text="Characteristics", width=20, height=2, command=lambda: pageSwitch("Characteristics"))
characteristicButton.grid(row=143, column=1, rowspan=142, columnspan=55, padx=(25,10))

skillsButton = Button(master, text="Skills", width=20, height=2, command=lambda: pageSwitch("Skills"))
skillsButton.grid(row=285, column=1, columnspan=55, rowspan=142, padx=(25,10))

perkTalentButton = Button(master, text="Perks/Talents", width=20, height=2, command=lambda: pageSwitch("Perks/Talents"))
perkTalentButton.grid(row=427, column=1, columnspan=55, rowspan=142, padx=(25,10))

powerButton = Button(master, text="Powers", width=20, height=2, command=lambda: pageSwitch("Powers"))
powerButton.grid(row=569, column=1, columnspan=55, rowspan=142, padx=(25,10))

complicationButton = Button(master, text="Complications", width=20, height=2, command=lambda: pageSwitch("Complications"))
complicationButton.grid(row=711, column=1, columnspan=55, rowspan=142, padx=(25,10))

charSheetButton = Button(master, text="Character Sheet", width=20, height=2, command=lambda: pageSwitch("Character Sheet"))
charSheetButton.grid(row=853, column=1, columnspan=55, rowspan=142, padx=(25,10))

testText = Text(master, height=1, width = 20)
testText.grid(row=200, column=100)
testText.insert(INSERT, "Character Details")

mainloop()
