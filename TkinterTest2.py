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

def retrieveCurrentValues():
    print(nameContent.get())
    print(sexContent.get())
    print(heightContent.get())
    print(massContent.get())
    print(skinContent.get())
    print(hairContent.get())
    print(eyesContent.get())
    print(ageContent.get())
    print(speciesContent.get())
    print(notesContent.get())
    print(pointTotalContent.get())
    print(activePointLimitContent.get())
    print(complicationPointsContent.get())
    print(strMaximaContent.get())
    print(dexMaximaContent.get())
    print(conMaximaContent.get())
    print(intMaximaContent.get())
    print(egoMaximaContent.get())
    print(preMaximaContent.get())
    print(ocvMaximaContent.get())
    print(dcvMaximaContent.get())
    print(omcvMaximaContent.get())
    print(dmcvMaximaContent.get())
    print(spdMaximaContent.get())
    print(pdMaximaContent.get())
    print(edMaximaContent.get())
    print(recMaximaContent.get())
    print(endMaximaContent.get())
    print(bodyMaximaContent.get())
    print(stunMaximaContent.get())
    print(runMaximaContent.get())
    print(swimMaximaContent.get())
    print(leapMaximaContent.get())
    print(skillMaximaContent.get())
    
def drawCharDetailsPage():
    spacer0 = Text(master, height=1, width=2)
    spacer0.grid(row=45, column=61)
    spacer0.config(state=DISABLED)

    nameText = Text(master, height=1, width=7)
    nameText.grid(row=45, column=62, columnspan=7)
    nameText.insert(INSERT, "Name")
    nameText.config(state=DISABLED) 
    global nameContent
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
    global sexContent
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
    global heightContent
    heightContent = StringVar()
    heightEntry = Entry(master, textvariable=heightContent, width=17)
    heightEntry.grid(row=45, column=119, columnspan=17)
    heightEntry.insert(0, """5'6" """)



    massText = Text(master, height=1, width=7)
    massText.grid(row=90, column=62, columnspan=7)
    massText.insert(INSERT, "Mass")
    massText.config(state=DISABLED) 
    global massContent
    massContent = StringVar()
    massEntry = Entry(master, textvariable=massContent, width=17)
    massEntry.grid(row=90, column=69, columnspan=17)
    massEntry.insert(0, "200 kg")

    skinText = Text(master, height=1, width=7)
    skinText.grid(row=90, column=87, columnspan=7)
    skinText.insert(INSERT, "Skin")
    skinText.config(state=DISABLED) 
    global skinContent
    skinContent = StringVar()
    skinEntry = Entry(master, textvariable=skinContent, width=17)
    skinEntry.grid(row=90, column=94, columnspan=17)
    skinEntry.insert(0, "Red Scales")

    hairText = Text(master, height=1, width=7)
    hairText.grid(row=90, column=112, columnspan=7)
    hairText.insert(INSERT, "Hair")
    hairText.config(state=DISABLED) 
    global hairContent
    hairContent = StringVar()
    hairEntry = Entry(master, textvariable=hairContent, width=17)
    hairEntry.grid(row=90, column=119, columnspan=17)
    hairEntry.insert(0, "Bald")



    eyesText = Text(master, height=1, width=7)
    eyesText.grid(row=135, column=62, columnspan=7)
    eyesText.insert(INSERT, "Eyes")
    eyesText.config(state=DISABLED) 
    global eyesContent
    eyesContent = StringVar()
    eyesEntry = Entry(master, textvariable=eyesContent, width=17)
    eyesEntry.grid(row=135, column=69, columnspan=17)
    eyesEntry.insert(0, "Snakey Yellow")

    ageText = Text(master, height=1, width=7)
    ageText.grid(row=135, column=87, columnspan=7)
    ageText.insert(INSERT,"Age")
    ageText.config(state=DISABLED) 
    global ageContent
    ageContent = StringVar()
    ageEntry = Entry(master, textvariable=ageContent, width=17)
    ageEntry.grid(row=135, column=94, columnspan=17)
    ageEntry.insert(0, "362")

    speciesText = Text(master, height=1, width=7)
    speciesText.grid(row=135, column=112, columnspan=7)
    speciesText.insert(INSERT, "Species")
    speciesText.config(state=DISABLED) 
    global speciesContent
    speciesContent = StringVar()
    speciesEntry = Entry(master, textvariable=speciesContent, width=17)
    speciesEntry.grid(row=135, column=119, columnspan=17)
    speciesEntry.insert(0, "Gronian")
    


    notesText = Text(master, height=1, width = 7)
    notesText.grid(row=180, column=62, columnspan=7)
    notesText.insert(INSERT, "Notes")
    notesText.config(state=DISABLED) 
    global notesContent
    notesContent = StringVar()
    notesEntry = Entry(master, textvariable=notesContent, width=91)
    notesEntry.grid(row=180, column = 69, columnspan = 91)
    notesEntry.insert(0, "Just insert some notes about the character here. Any fluff details that don't fit in the categories above.")


    
    pointTotalText = Text(master, height=1, width = 21)
    pointTotalText.grid(row=270, column=62, columnspan=21, sticky=W)
    pointTotalText.insert(INSERT, "Point Limit")
    pointTotalText.config(state=DISABLED) 
    global pointTotalContent
    pointTotalContent = StringVar()
    pointTotalEntry = Entry(master, textvariable=pointTotalContent, width=3)
    pointTotalEntry.grid(row=270, column = 83, columnspan=3)
    pointTotalEntry.insert(0, "400")

    activePointLimitText = Text(master, height=1, width = 21)
    activePointLimitText.grid(row=270, column=87, columnspan=21, sticky=W)
    activePointLimitText.insert(INSERT,"Active Point Limit")
    activePointLimitText.config(state=DISABLED) 
    global activePointLimitContent
    activePointLimitContent = StringVar()
    activePointLimitEntry = Entry(master, textvariable=activePointLimitContent, width=3)
    activePointLimitEntry.grid(row=270, column = 108, columnspan=3)
    activePointLimitEntry.insert(0, "100")

    complicationPointsText = Text(master, height=1, width = 21)
    complicationPointsText.grid(row=270, column=112, columnspan=21, sticky=W)
    complicationPointsText.insert(INSERT, "Complication Points")
    complicationPointsText.config(state=DISABLED) 
    global complicationPointsContent
    complicationPointsContent = StringVar()
    complicationPointsEntry = Entry(master, textvariable=complicationPointsContent, width=3)
    complicationPointsEntry.grid(row=270, column = 133, columnspan=3)
    complicationPointsEntry.insert(0, "100")



    maximaText = Text(master, height=1, width = 7)
    maximaText.grid(row=360, column=62, columnspan=37, sticky=E)
    maximaText.insert(INSERT, "Maxima?")
    maximaText.config(state=DISABLED)
    var = IntVar()
    maximaCheckBox = Checkbutton(master, variable=var)
    maximaCheckBox.grid(row=360, column=99)
    
    

    strMaximaText = Text(master, height=1, width = 21)
    strMaximaText.grid(row=405, column=62, columnspan=21, sticky=W)
    strMaximaText.insert(INSERT, "Strength Maxima")
    strMaximaText.config(state=DISABLED)
    global strMaximaContent
    strMaximaContent = StringVar()
    strMaximaEntry = Entry(master, textvariable=strMaximaContent, width=3)
    strMaximaEntry.grid(row=405, column = 83, columnspan=3)
    strMaximaEntry.insert(0, "100")

    dexMaximaText = Text(master, height=1, width = 21)
    dexMaximaText.grid(row=405, column=87, columnspan=21, sticky=W)
    dexMaximaText.insert(INSERT,"Dexterity Maxima")
    dexMaximaText.config(state=DISABLED)
    global dexMaximaContent
    dexMaximaContent = StringVar()
    dexMaximaEntry = Entry(master, textvariable=dexMaximaContent, width=3)
    dexMaximaEntry.grid(row=405, column = 108, columnspan=3)
    dexMaximaEntry.insert(0, "100")

    conMaximaText = Text(master, height=1, width = 21)
    conMaximaText.grid(row=405, column=112, columnspan=21, sticky=W)
    conMaximaText.insert(INSERT, "Constitution Maxima")
    conMaximaText.config(state=DISABLED)
    global conMaximaContent
    conMaximaContent = StringVar()
    conMaximaEntry = Entry(master, textvariable=conMaximaContent, width=3)
    conMaximaEntry.grid(row=405, column = 133, columnspan=3)
    conMaximaEntry.insert(0, "100")



    intMaximaText = Text(master, height=1, width = 21)
    intMaximaText.grid(row=450, column=62, columnspan=21, sticky=W)
    intMaximaText.insert(INSERT, "Intelligence Maxima")
    intMaximaText.config(state=DISABLED)
    global intMaximaContent
    intMaximaContent = StringVar()
    intMaximaEntry = Entry(master, textvariable=intMaximaContent, width=3)
    intMaximaEntry.grid(row=450, column = 83, columnspan=3)
    intMaximaEntry.insert(0, "100")

    egoMaximaText = Text(master, height=1, width = 21)
    egoMaximaText.grid(row=450, column=87, columnspan=21, sticky=W)
    egoMaximaText.insert(INSERT,"Ego Maxima")
    egoMaximaText.config(state=DISABLED)
    global egoMaximaContent
    egoMaximaContent = StringVar()
    egoMaximaEntry = Entry(master, textvariable=egoMaximaContent, width=3)
    egoMaximaEntry.grid(row=450, column = 108, columnspan=3)
    egoMaximaEntry.insert(0, "100")

    preMaximaText = Text(master, height=1, width = 21)
    preMaximaText.grid(row=450, column=112, columnspan=21, sticky=W)
    preMaximaText.insert(INSERT, "Presence Maxima")
    preMaximaText.config(state=DISABLED)
    global preMaximaContent
    preMaximaContent = StringVar()
    preMaximaEntry = Entry(master, textvariable=preMaximaContent, width=3)
    preMaximaEntry.grid(row=450, column = 133, columnspan=3)
    preMaximaEntry.insert(0, "100")



    ocvMaximaText = Text(master, height=1, width = 21)
    ocvMaximaText.grid(row=495, column=62, columnspan=21, sticky=W)
    ocvMaximaText.insert(INSERT, "OCV Maxima")
    ocvMaximaText.config(state=DISABLED)
    global ocvMaximaContent
    ocvMaximaContent = StringVar()
    ocvMaximaEntry = Entry(master, textvariable=ocvMaximaContent, width=3)
    ocvMaximaEntry.grid(row=495, column = 83, columnspan=3)
    ocvMaximaEntry.insert(0, "100")

    dcvMaximaText = Text(master, height=1, width = 21)
    dcvMaximaText.grid(row=495, column=87, columnspan=21, sticky=W)
    dcvMaximaText.insert(INSERT,"DCV Maxima")
    dcvMaximaText.config(state=DISABLED)
    global dcvMaximaContent
    dcvMaximaContent = StringVar()
    dcvMaximaEntry = Entry(master, textvariable=dcvMaximaContent, width=3)
    dcvMaximaEntry.grid(row=495, column = 108, columnspan=3)
    dcvMaximaEntry.insert(0, "100")

    omcvMaximaText = Text(master, height=1, width = 21)
    omcvMaximaText.grid(row=495, column=112, columnspan=21, sticky=W)
    omcvMaximaText.insert(INSERT, "OMCV Maxima")
    omcvMaximaText.config(state=DISABLED)
    global omcvMaximaContent
    omcvMaximaContent = StringVar()
    omcvMaximaEntry = Entry(master, textvariable=omcvMaximaContent, width=3)
    omcvMaximaEntry.grid(row=495, column = 133, columnspan=3)
    omcvMaximaEntry.insert(0, "100")



    dmcvMaximaText = Text(master, height=1, width = 21)
    dmcvMaximaText.grid(row=540, column=62, columnspan=21, sticky=W)
    dmcvMaximaText.insert(INSERT, "DMCV Maxima")
    dmcvMaximaText.config(state=DISABLED)
    global dmcvMaximaContent
    dmcvMaximaContent = StringVar()
    dmcvMaximaEntry = Entry(master, textvariable=dmcvMaximaContent, width=3)
    dmcvMaximaEntry.grid(row=540, column = 83, columnspan=3)
    dmcvMaximaEntry.insert(0, "100")

    spdMaximaText = Text(master, height=1, width = 21)
    spdMaximaText.grid(row=540, column=87, columnspan=21, sticky=W)
    spdMaximaText.insert(INSERT,"Speed Maxima")
    spdMaximaText.config(state=DISABLED)
    global spdMaximaContent
    spdMaximaContent = StringVar()
    spdMaximaEntry = Entry(master, textvariable=spdMaximaContent, width=3)
    spdMaximaEntry.grid(row=540, column = 108, columnspan=3)
    spdMaximaEntry.insert(0, "100")

    pdMaximaText = Text(master, height=1, width = 21)
    pdMaximaText.grid(row=540, column=112, columnspan=21, sticky=W)
    pdMaximaText.insert(INSERT, "Physical Defense Maxima")
    pdMaximaText.config(state=DISABLED)
    global pdMaximaContent
    pdMaximaContent = StringVar()
    pdMaximaEntry = Entry(master, textvariable=pdMaximaContent, width=3)
    pdMaximaEntry.grid(row=540, column = 133, columnspan=3)
    pdMaximaEntry.insert(0, "100")



    edMaximaText = Text(master, height=1, width = 21)
    edMaximaText.grid(row=585, column=62, columnspan=21, sticky=W)
    edMaximaText.insert(INSERT, "Energy Defense Maxima")
    edMaximaText.config(state=DISABLED)
    global edMaximaContent
    edMaximaContent = StringVar()
    edMaximaEntry = Entry(master, textvariable=edMaximaContent, width=3)
    edMaximaEntry.grid(row=585, column = 83, columnspan=3)
    edMaximaEntry.insert(0, "100")

    recMaximaText = Text(master, height=1, width = 21)
    recMaximaText.grid(row=585, column=87, columnspan=21, sticky=W)
    recMaximaText.insert(INSERT,"Recovery Maxima")
    recMaximaText.config(state=DISABLED)
    global recMaximaContent
    recMaximaContent = StringVar()
    recMaximaEntry = Entry(master, textvariable=recMaximaContent, width=3)
    recMaximaEntry.grid(row=585, column = 108, columnspan=3)
    recMaximaEntry.insert(0, "100")

    endMaximaText = Text(master, height=1, width = 21)
    endMaximaText.grid(row=585, column=112, columnspan=21, sticky=W)
    endMaximaText.insert(INSERT, "Endurance Maxima")
    endMaximaText.config(state=DISABLED)
    global endMaximaContent
    endMaximaContent = StringVar()
    endMaximaEntry = Entry(master, textvariable=endMaximaContent, width=3)
    endMaximaEntry.grid(row=585, column = 133, columnspan=3)
    endMaximaEntry.insert(0, "100")



    bodyMaximaText = Text(master, height=1, width = 21)
    bodyMaximaText.grid(row=630, column=62, columnspan=21, sticky=W)
    bodyMaximaText.insert(INSERT, "Body Maxima")
    bodyMaximaText.config(state=DISABLED)
    global bodyMaximaContent
    bodyMaximaContent = StringVar()
    bodyMaximaEntry = Entry(master, textvariable=bodyMaximaContent, width=3)
    bodyMaximaEntry.grid(row=630, column = 83, columnspan=3)
    bodyMaximaEntry.insert(0, "100")

    stunMaximaText = Text(master, height=1, width = 21)
    stunMaximaText.grid(row=630, column=87, columnspan=21, sticky=W)
    stunMaximaText.insert(INSERT,"Stun Maxima")
    stunMaximaText.config(state=DISABLED)
    global stunMaximaContent
    stunMaximaContent = StringVar()
    stunMaximaEntry = Entry(master, textvariable=stunMaximaContent, width=3)
    stunMaximaEntry.grid(row=630, column = 108, columnspan=3)
    stunMaximaEntry.insert(0, "100")

    runMaximaText = Text(master, height=1, width = 21)
    runMaximaText.grid(row=630, column=112, columnspan=21, sticky=W)
    runMaximaText.insert(INSERT, "Run Speed Maxima")
    runMaximaText.config(state=DISABLED)
    global runMaximaContent
    runMaximaContent = StringVar()
    runMaximaEntry = Entry(master, textvariable=runMaximaContent, width=3)
    runMaximaEntry.grid(row=630, column = 133, columnspan=3)
    runMaximaEntry.insert(0, "100")



    swimMaximaText = Text(master, height=1, width = 21)
    swimMaximaText.grid(row=675, column=62, columnspan=21, sticky=W)
    swimMaximaText.insert(INSERT, "Swim Speed Maxima")
    swimMaximaText.config(state=DISABLED)
    global swimMaximaContent
    swimMaximaContent = StringVar()
    swimMaximaEntry = Entry(master, textvariable=swimMaximaContent, width=3)
    swimMaximaEntry.grid(row=675, column = 83, columnspan=3)
    swimMaximaEntry.insert(0, "100")

    leapMaximaText = Text(master, height=1, width = 21)
    leapMaximaText.grid(row=675, column=87, columnspan=21, sticky=W)
    leapMaximaText.insert(INSERT,"Leap Distance Maxima")
    leapMaximaText.config(state=DISABLED)
    global leapMaximaContent
    leapMaximaContent = StringVar()
    leapMaximaEntry = Entry(master, textvariable=leapMaximaContent, width=3)
    leapMaximaEntry.grid(row=675, column = 108, columnspan=3)
    leapMaximaEntry.insert(0, "100")

    skillMaximaText = Text(master, height=1, width = 21)
    skillMaximaText.grid(row=675, column=112, columnspan=21, sticky=W)
    skillMaximaText.insert(INSERT, "Skill Maxima")
    skillMaximaText.config(state=DISABLED)
    global skillMaximaContent
    skillMaximaContent = StringVar()
    skillMaximaEntry = Entry(master, textvariable=skillMaximaContent, width=3)
    skillMaximaEntry.grid(row=675, column = 133, columnspan=3)
    skillMaximaEntry.insert(0, "100")

    submitButton = Button(master, text="Submit", command=retrieveCurrentValues)
    submitButton.grid(row=765, column=62, columnspan=74)
    
drawCharDetailsPage()


mainloop()
