from tkinter import *

master = Tk()
master.geometry('1000x1000')

w = Canvas(master, width=5, height=952)

def pageSwitch(newPage):
    testText.delete(1.0, END)
    testText.insert(INSERT, newPage)

w.grid(row=0, column=56, rowspan=952, columnspan=5)
w.create_line(5, 0, 5, 952, fill="#000000", width=5)

photo=PhotoImage(file="Test.gif")
charDetailsButton = Button(master, image=photo, width=160, height = 127, command=lambda: pageSwitch("Character Details"))
charDetailsButton.grid(row=0, column=1, rowspan=136, columnspan=55, padx=(25,10))

#characteristicButton = Button(master, text="Characteristics", width=20, height=0, command=lambda: pageSwitch("Characteristics"))
characteristicButton = Button(master, image=photo, width=160, height=127, command=lambda: pageSwitch("Characteristics"))
characteristicButton.grid(row=137, column=1, rowspan=136, columnspan=55, padx=(25,10))

skillsButton = Button(master, image=photo, width=160, height=127, command=lambda: pageSwitch("Skills"))
skillsButton.grid(row=273, column=1, columnspan=55, rowspan=136, padx=(25,10))

perkTalentButton = Button(master, image=photo, width=160, height=127, command=lambda: pageSwitch("Perks/Talents"))
perkTalentButton.grid(row=409, column=1, columnspan=55, rowspan=136, padx=(25,10))

powerButton = Button(master, image=photo, width=160, height=127, command=lambda: pageSwitch("Powers"))
powerButton.grid(row=545, column=1, columnspan=55, rowspan=136, padx=(25,10))

complicationButton = Button(master, image=photo, width=160, height=127, command=lambda: pageSwitch("Complications"))
complicationButton.grid(row=681, column=1, columnspan=55, rowspan=136, padx=(25,10))

charSheetButton = Button(master, image=photo, width=160, height=127, command=lambda: pageSwitch("Character Sheet"))
charSheetButton.grid(row=817, column=1, columnspan=55, rowspan=136, padx=(25,10))

testText = Text(master, height=1, width = 20)
testText.grid(row=200, column=100)
testText.insert(INSERT, "Character Details")

mainloop()
