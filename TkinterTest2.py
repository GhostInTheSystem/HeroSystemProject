from tkinter import *

master = Tk()
master.geometry('952x952')

w = Canvas(master, width=5, height=952)

w.grid(row=0, column=56, rowspan=952, columnspan=5)
w.create_line(5, 0, 5, 950, fill="#000000", width=5)

def pageSwitch(newPage):
    testText.delete(1.0, END)
    testText.insert(INSERT, newPage)

photo=PhotoImage(file="Test.gif")
def drawTabSystem():
    charDetailsButton = Button(master, image=photo, width=160, height = 127, command=lambda: pageSwitch("Character Details"))
    charDetailsButton.grid(row=0, column=1, rowspan=136, columnspan=55, padx=(25,10))

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
drawTabSystem()

#testButton = Button(master, text="Click Me", width=10, height=1, command=lambda: printTextBox())
#testButton.grid(row=0, column=61)


def drawCharDetailsPage():
    spacer0 = Text(master, height=1, width = 2)
    spacer0.grid(row=45, column=61)
    spacer0.config(state=DISABLED)

    nameText = Text(master, height=1, width = 7)
    nameText.grid(row=45, column=62)
    nameText.insert(INSERT, "Name")
    nameText.config(state=DISABLED)
    nameContent = StringVar()
    nameEntry = Entry(master, textvariable=nameContent, width=17)
    nameEntry.grid(row=45, column = 63)
    nameEntry.insert(0, "Captain Kharok")

    spacer1 = Text(master, height=1, width = 9)
    spacer1.grid(row=45, column=64)
    spacer1.config(state=DISABLED)

    sexText = Text(master, height=1, width = 7)
    sexText.grid(row=45, column=65)
    sexText.insert(INSERT, "Sex")
    sexText.config(state=DISABLED)
    sexContent = StringVar()
    sexEntry = Entry(master, textvariable=sexContent, width=17)
    sexEntry.grid(row=45, column = 66)
    sexEntry.insert(0, "Male")

    spacer2 = Text(master, height=1, width = 9)
    spacer2.grid(row=45, column=67)
    spacer2.config(state=DISABLED)

    heightText = Text(master, height=1, width = 7)
    heightText.grid(row=45, column=68)
    heightText.insert(INSERT, "Height")
    heightText.config(state=DISABLED)
    heightContent = StringVar()
    heightEntry = Entry(master, textvariable=heightContent, width=17)
    heightEntry.grid(row=45, column = 69)
    heightEntry.insert(0, """5'6" """)



drawCharDetailsPage()
'''
Fluff:
    Name
    Sex
    Height
    Mass
    Skin
    Hair
    Eyes
    Age
    Species
    Notes
Crunch:
    Point Total
    Active Point Limit
    Complication Points
    Maxima?
'''


testText = Text(master, height=1, width = 20)
testText.grid(row=200, column=100)
testText.insert(INSERT, "Character Details")

mainloop()
