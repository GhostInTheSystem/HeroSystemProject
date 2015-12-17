from tkinter import *

master = Tk()
master.geometry('1000x1000')

w = Canvas(master, width=5, height=1000)


w.grid(row=0, column=2, rowspan=7)
w.create_line(5, 0, 5, 1000, fill="#000000", width=5)


charDetailsButton = Button(master, text="Character Details", width=20, height=2)
charDetailsButton.grid(row=0, column=1, padx=(25,10))

characteristicButton = Button(master, text="Characteristics", width=20, height=2)
characteristicButton.grid(row=1, column=1, padx=(25,10))

skillsButton = Button(master, text="Skills", width=20, height=2)
skillsButton.grid(row=2, column=1, padx=(25,10))

perkTalentButton = Button(master, text="Perks/Talents", width=20, height=2)
perkTalentButton.grid(row=3, column=1, padx=(25,10))

powerButton = Button(master, text="Powers", width=20, height=2)
powerButton.grid(row=4, column=1, padx=(25,10))

complicationButton = Button(master, text="Complications", width=20, height=2)
complicationButton.grid(row=5, column=1, padx=(25,10))

charSheetButton = Button(master, text="Character Sheet", width=20, height=2)
charSheetButton.grid(row=6, column=1, padx=(25,10))


outText = Label(master, text="Sample Output")
outText.grid(row = 4, column = 3)

mainloop()
