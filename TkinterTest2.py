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
    spacer0 = Text(master, height=1, width=2)
    spacer0.grid(row=45, column=61)
    spacer0.config(state=DISABLED)

    nameText = Text(master, height=1, width=7)
    nameText.grid(row=45, column=62, columnspan=7)
    nameText.insert(INSERT, "Name")
    nameText.config(state=DISABLED)
    nameContent = StringVar()
    nameEntry = Entry(master, textvariable=nameContent, width=17)
    nameEntry.grid(row=45, column=69, columnspan=17)
    nameEntry.insert(0, "Captain Kharok")

    spacer1 = Text(master, height=1, width=9)
    spacer1.grid(row=45, column=86)
    spacer1.config(state=DISABLED)

    sexText = Text(master, height=1, width=7)
    sexText.grid(row=45, column=87, columnspan=7)
    sexText.insert(INSERT, "Sex")
    sexText.config(state=DISABLED)
    sexContent = StringVar()
    sexEntry = Entry(master, textvariable=sexContent, width=17)
    sexEntry.grid(row=45, column=94, columnspan=17)
    sexEntry.insert(0, "Male")

    spacer2 = Text(master, height=1, width=9)
    spacer2.grid(row=45, column=111)
    spacer2.config(state=DISABLED)

    heightText = Text(master, height=1, width=7)
    heightText.grid(row=45, column=112, columnspan=7)
    heightText.insert(INSERT, "Height")
    heightText.config(state=DISABLED)
    heightContent = StringVar()
    heightEntry = Entry(master, textvariable=heightContent, width=17)
    heightEntry.grid(row=45, column=119, columnspan=17)
    heightEntry.insert(0, """5'6" """)



    spacer3 = Text(master, height=1, width=2)
    spacer3.grid(row=90, column=61)
    spacer3.config(state=DISABLED)

    massText = Text(master, height=1, width=7)
    massText.grid(row=90, column=62, columnspan=7)
    massText.insert(INSERT, "Mass")
    massText.config(state=DISABLED)
    massContent = StringVar()
    massEntry = Entry(master, textvariable=massContent, width=17)
    massEntry.grid(row=90, column=69, columnspan=17)
    massEntry.insert(0, "200 kg")

    spacer4 = Text(master, height=1, width=9)
    spacer4.grid(row=90, column=86)
    spacer4.config(state=DISABLED)

    skinText = Text(master, height=1, width=7)
    skinText.grid(row=90, column=87, columnspan=7)
    skinText.insert(INSERT, "Skin")
    skinText.config(state=DISABLED)
    skinContent = StringVar()
    skinEntry = Entry(master, textvariable=skinContent, width=17)
    skinEntry.grid(row=90, column=94, columnspan=17)
    skinEntry.insert(0, "Red Scales")

    spacer5 = Text(master, height=1, width=9)
    spacer5.grid(row=90, column=111)
    spacer5.config(state=DISABLED)

    hairText = Text(master, height=1, width=7)
    hairText.grid(row=90, column=112, columnspan=7)
    hairText.insert(INSERT, "Hair")
    hairText.config(state=DISABLED)
    hairContent = StringVar()
    hairEntry = Entry(master, textvariable=hairContent, width=17)
    hairEntry.grid(row=90, column=119, columnspan=17)
    hairEntry.insert(0, "Bald")


    spacer6 = Text(master, height=1, width=2)
    spacer6.grid(row=135, column=61)
    spacer6.config(state=DISABLED)

    eyesText = Text(master, height=1, width=7)
    eyesText.grid(row=135, column=62, columnspan=7)
    eyesText.insert(INSERT, "Eyes")
    eyesText.config(state=DISABLED)
    eyesContent = StringVar()
    eyesEntry = Entry(master, textvariable=eyesContent, width=17)
    eyesEntry.grid(row=135, column=69, columnspan=17)
    eyesEntry.insert(0, "Snakey Yellow")

    spacer7 = Text(master, height=1, width=9)
    spacer7.grid(row=135, column=86)
    spacer7.config(state=DISABLED)

    ageText = Text(master, height=1, width=7)
    ageText.grid(row=135, column=87, columnspan=7)
    ageText.insert(INSERT,"Age")
    ageText.config(state=DISABLED)
    ageContent = StringVar()
    ageEntry = Entry(master, textvariable=ageContent, width=17)
    ageEntry.grid(row=135, column=94, columnspan=17)
    ageEntry.insert(0, "362")

    spacer8 = Text(master, height=1, width=9)
    spacer8.grid(row=135, column=111)
    spacer8.config(state=DISABLED)

    speciesText = Text(master, height=1, width=7)
    speciesText.grid(row=135, column=112, columnspan=7)
    speciesText.insert(INSERT, "Species")
    speciesText.config(state=DISABLED)
    speciesContent = StringVar()
    speciesEntry = Entry(master, textvariable=speciesContent, width=17)
    speciesEntry.grid(row=135, column=119, columnspan=17)
    speciesEntry.insert(0, "Gronian")
    


    '''
    spacer9 = Text(master, height=1, width = 2)
    spacer9.grid(row=180, column=61)
    spacer9.config(state=DISABLED)

    notesText = Text(master, height=1, width = 7)
    notesText.grid(row=180, column=62)
    notesText.insert(INSERT, "Notes")
    notesText.config(state=DISABLED)
    notesContent = StringVar()
    notesEntry = Entry(master, textvariable=notesContent, width=91)
    notesEntry.grid(row=180, column = 63, columnspan = 7)
    notesEntry.insert(0, "Just insert some notes about the character here. Any fluff details that don't fit in the categories above.")



    spacer10 = Text(master, height=1, width = 2)
    spacer10.grid(row=270, column=61)
    spacer10.config(state=DISABLED)

    pointTotalText = Text(master, height=1, width = 21)
    pointTotalText.grid(row=270, column=62)
    pointTotalText.insert(INSERT, "Point Limit")
    pointTotalText.config(state=DISABLED)
    pointTotalContent = StringVar()
    pointTotalEntry = Entry(master, textvariable=pointTotalContent, width=3)
    pointTotalEntry.grid(row=270, column = 63)
    pointTotalEntry.insert(0, "400")

    spacer11 = Text(master, height=1, width = 9)
    spacer11.grid(row=270, column=64)
    spacer11.config(state=DISABLED)

    activePointLimitText = Text(master, height=1, width = 21)
    activePointLimitText.grid(row=270, column=65)
    activePointLimitText.insert(INSERT,"Active Point Limit")
    activePointLimitText.config(state=DISABLED)
    activePointLimitContent = StringVar()
    activePointLimitEntry = Entry(master, textvariable=activePointLimitContent, width=3)
    activePointLimitEntry.grid(row=270, column = 66)
    activePointLimitEntry.insert(0, "100")

    spacer12 = Text(master, height=1, width = 9)
    spacer12.grid(row=270, column=67)
    spacer12.config(state=DISABLED)

    complicationPointsText = Text(master, height=1, width = 21)
    complicationPointsText.grid(row=270, column=68)
    complicationPointsText.insert(INSERT, "Complication Points")
    complicationPointsText.config(state=DISABLED)
    complicationPointsContent = StringVar()
    complicationPointsEntry = Entry(master, textvariable=complicationPointsContent, width=3)
    complicationPointsEntry.grid(row=270, column = 69)
    complicationPointsEntry.insert(0, "100")
    '''


    
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

mainloop()
