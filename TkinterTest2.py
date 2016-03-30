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

def drawCharDetailsPage():
    global spacer0
    global spacer1
    global spacer2
    global nameText
    global nameEntry
    global sexText
    global sexEntry
    global heightText
    global heightEntry
    global massText
    global massEntry
    global skinText
    global skinEntry
    global hairText
    global hairEntry
    global eyesText
    global eyesEntry
    global ageText
    global ageEntry
    global speciesText
    global speciesEntry
    global notesText
    global notesEntry
    global pointTotalText
    global pointTotalEntry
    global activePointLimitText
    global activePointLimitEntry
    global complicationPointsText
    global complicationPointsEntry
    global maximaText
    global maximaCheckBox
    global strMaximaText
    global strMaximaEntry
    global dexMaximaText
    global dexMaximaEntry
    global conMaximaText
    global conMaximaEntry
    global intMaximaText
    global intMaximaEntry
    global egoMaximaText
    global egoMaximaEntry
    global preMaximaText
    global preMaximaEntry
    global ocvMaximaText
    global ocvMaximaEntry
    global dcvMaximaText
    global dcvMaximaEntry
    global omcvMaximaText
    global omcvMaximaEntry
    global dmcvMaximaText
    global dmcvMaximaEntry
    global spdMaximaText
    global spdMaximaEntry
    global pdMaximaText
    global pdMaximaEntry
    global edMaximaText
    global edMaximaEntry
    global recMaximaText
    global recMaximaEntry
    global endMaximaText
    global endMaximaEntry
    global bodyMaximaText
    global bodyMaximaEntry
    global stunMaximaText
    global stunMaximaEntry
    global runMaximaText
    global runMaximaEntry
    global swimMaximaText
    global swimMaximaEntry
    global leapMaximaText
    global leapMaximaEntry
    global skillMaximaText
    global skillMaximaEntry



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
    global maximaContent
    maximaContent = IntVar()
    maximaCheckBox = Checkbutton(master, variable=maximaContent)
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

    submitButton = Button(master, text="Submit", command=lambda: retrieveCurrentValues("CharDetails"))
    submitButton.grid(row=765, column=62, columnspan=74)

def eraseCharDetailsPage():
    spacer0.grid_forget()
    spacer1.grid_forget()
    spacer2.grid_forget()
    nameText.grid_forget()
    nameEntry.grid_forget()
    sexText.grid_forget()
    sexEntry.grid_forget()
    heightText.grid_forget()
    heightEntry.grid_forget()
    massText.grid_forget()
    massEntry.grid_forget()
    skinText.grid_forget()
    skinEntry.grid_forget()
    hairText.grid_forget()
    hairEntry.grid_forget()
    eyesText.grid_forget()
    eyesEntry.grid_forget()
    ageText.grid_forget()
    ageEntry.grid_forget()
    speciesText.grid_forget()
    speciesEntry.grid_forget()
    notesText.grid_forget()
    notesEntry.grid_forget()
    pointTotalText.grid_forget()
    pointTotalEntry.grid_forget()
    activePointLimitText.grid_forget()
    activePointLimitEntry.grid_forget()
    complicationPointsText.grid_forget()
    complicationPointsEntry.grid_forget()
    maximaText.grid_forget()
    maximaCheckBox.grid_forget()
    strMaximaText.grid_forget()
    strMaximaEntry.grid_forget()
    dexMaximaText.grid_forget()
    dexMaximaEntry.grid_forget()
    conMaximaText.grid_forget()
    conMaximaEntry.grid_forget()
    intMaximaText.grid_forget()
    intMaximaEntry.grid_forget()
    egoMaximaText.grid_forget()
    egoMaximaEntry.grid_forget()
    preMaximaText.grid_forget()
    preMaximaEntry.grid_forget()
    ocvMaximaText.grid_forget()
    ocvMaximaEntry.grid_forget()
    dcvMaximaText.grid_forget()
    dcvMaximaEntry.grid_forget()
    omcvMaximaText.grid_forget()
    omcvMaximaEntry.grid_forget()
    dmcvMaximaText.grid_forget()
    dmcvMaximaEntry.grid_forget()
    spdMaximaText.grid_forget()
    spdMaximaEntry.grid_forget()
    pdMaximaText.grid_forget()
    pdMaximaEntry.grid_forget()
    edMaximaText.grid_forget()
    edMaximaEntry.grid_forget()
    recMaximaText.grid_forget()
    recMaximaEntry.grid_forget()
    endMaximaText.grid_forget()
    endMaximaEntry.grid_forget()
    bodyMaximaText.grid_forget()
    bodyMaximaEntry.grid_forget()
    stunMaximaText.grid_forget()
    stunMaximaEntry.grid_forget()
    runMaximaText.grid_forget()
    runMaximaEntry.grid_forget()
    swimMaximaText.grid_forget()
    swimMaximaEntry.grid_forget()
    leapMaximaText.grid_forget()
    leapMaximaEntry.grid_forget()
    skillMaximaText.grid_forget()
    skillMaximaEntry.grid_forget()


def retrieveCurrentValues(page):
    if(page=="CharDetails"): 
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
        print(maximaContent.get())
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
    elif(page=="Characteristics"):
        print(strContent.get())
        print(dexContent.get())
        print(conContent.get())
        print(intContent.get())
        print(egoContent.get())
        print(preContent.get())
        print(ocvContent.get())
        print(dcvContent.get())
        print(dmcvContent.get())
        print(omcvContent.get())
        print(spdContent.get())
        print(recContent.get())
        print(endContent.get())
        print(bodyContent.get())
        print(stunContent.get())
    
def drawCharacteristicsPage():
    spacer0 = Text(master, height=1, width=2)
    spacer0.grid(row=45, column=61)
    spacer0.config(state=DISABLED)

    strText = Text(master, height=1, width = 31)
    strText.grid(row=45, column=62, columnspan=31, sticky=W)
    strText.insert(INSERT, "Strength")
    strText.config(state=DISABLED)
    global strContent
    strContent = StringVar()
    strEntry = Entry(master, textvariable=strContent, width=5)
    strEntry.grid(row=45, column = 93, columnspan=5)
    strEntry.insert(0, "100")

    spacer1 = Text(master, height=1, width=9)
    spacer1.grid(row=45, column=98)
    spacer1.config(state=DISABLED)

    dexText = Text(master, height=1, width = 31)
    dexText.grid(row=45, column=99, columnspan=31, sticky=W)
    dexText.insert(INSERT,"Dexterity")
    dexText.config(state=DISABLED)
    global dexContent
    dexContent = StringVar()
    dexEntry = Entry(master, textvariable=dexContent, width=5)
    dexEntry.grid(row=45, column = 130, columnspan=5)
    dexEntry.insert(0, "100")

    strModButton = Button(master, text="Edit Mods", height=1, width=6)
    strModButton.grid(row=46, column=62, columnspan=6)
    
    strModFrame = Frame(master, bd=2, relief=SUNKEN)
    strModFrame.grid_rowconfigure(0, weight=1)
    strModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(strModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(strModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Points)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    strModFrame.grid(row=46, column=68, columnspan=30)

    dexModButton = Button(master, text="Edit Mods", height=1, width=6)
    dexModButton.grid(row=46, column=99, columnspan=6)

    dexModFrame = Frame(master, bd=2, relief=SUNKEN)
    dexModFrame.grid_rowconfigure(0, weight=1)
    dexModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(dexModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(dexModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Points)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    dexModFrame.grid(row=46, column=105, columnspan=30)



    conText = Text(master, height=1, width = 31)
    conText.grid(row=115, column=62, columnspan=31, sticky=W)
    conText.insert(INSERT, "Constitution")
    conText.config(state=DISABLED)
    global conContent
    conContent = StringVar()
    conEntry = Entry(master, textvariable=conContent, width=5)
    conEntry.grid(row=115, column = 93, columnspan=5)
    conEntry.insert(0, "100")

    intText = Text(master, height=1, width = 31)
    intText.grid(row=115, column=99, columnspan=31, sticky=W)
    intText.insert(INSERT,"Intelligence")
    intText.config(state=DISABLED)
    global intContent
    intContent = StringVar()
    intEntry = Entry(master, textvariable=intContent, width=5)
    intEntry.grid(row=115, column = 130, columnspan=5)
    intEntry.insert(0, "100")

    conModButton = Button(master, text="Edit Mods", height=1, width=6)
    conModButton.grid(row=116, column=62, columnspan=6)
    
    conModFrame = Frame(master, bd=2, relief=SUNKEN)
    conModFrame.grid_rowconfigure(0, weight=1)
    conModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(conModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(conModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    conModFrame.grid(row=116, column=68, columnspan=30)

    intModButton = Button(master, text="Edit Mods", height=1, width=6)
    intModButton.grid(row=116, column=99, columnspan=6)

    intModFrame = Frame(master, bd=2, relief=SUNKEN)
    intModFrame.grid_rowconfigure(0, weight=1)
    intModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(intModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(intModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    intModFrame.grid(row=116, column=105, columnspan=30)



    egoText = Text(master, height=1, width = 31)
    egoText.grid(row=145, column=62, columnspan=31, sticky=W)
    egoText.insert(INSERT, "Ego")
    egoText.config(state=DISABLED)
    global egoContent
    egoContent = StringVar()
    egoEntry = Entry(master, textvariable=egoContent, width=5)
    egoEntry.grid(row=145, column = 93, columnspan=5)
    egoEntry.insert(0, "100")

    preText = Text(master, height=1, width = 31)
    preText.grid(row=145, column=99, columnspan=31, sticky=W)
    preText.insert(INSERT,"Presence")
    preText.config(state=DISABLED)
    global preContent
    preContent = StringVar()
    preEntry = Entry(master, textvariable=preContent, width=5)
    preEntry.grid(row=145, column = 130, columnspan=5)
    preEntry.insert(0, "100")

    egoModButton = Button(master, text="Edit Mods", height=1, width=6)
    egoModButton.grid(row=146, column=62, columnspan=6)
    
    egoModFrame = Frame(master, bd=2, relief=SUNKEN)
    egoModFrame.grid_rowconfigure(0, weight=1)
    egoModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(egoModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(egoModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    egoModFrame.grid(row=146, column=68, columnspan=30)

    preModButton = Button(master, text="Edit Mods", height=1, width=6)
    preModButton.grid(row=146, column=99, columnspan=6)

    preModFrame = Frame(master, bd=2, relief=SUNKEN)
    preModFrame.grid_rowconfigure(0, weight=1)
    preModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(preModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(preModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    preModFrame.grid(row=146, column=105, columnspan=30)



    ocvText = Text(master, height=1, width = 31)
    ocvText.grid(row=325, column=62, columnspan=31, sticky=W)
    ocvText.insert(INSERT, "Offensive Combat Value")
    ocvText.config(state=DISABLED)
    global ocvContent
    ocvContent = StringVar()
    ocvEntry = Entry(master, textvariable=ocvContent, width=5)
    ocvEntry.grid(row=325, column = 93, columnspan=5)
    ocvEntry.insert(0, "100")

    dcvText = Text(master, height=1, width = 31)
    dcvText.grid(row=325, column=99, columnspan=31, sticky=W)
    dcvText.insert(INSERT,"Defensive Combat Value")
    dcvText.config(state=DISABLED)
    global dcvContent
    dcvContent = StringVar()
    dcvEntry = Entry(master, textvariable=dcvContent, width=5)
    dcvEntry.grid(row=325, column = 130, columnspan=5)
    dcvEntry.insert(0, "100")

    ocvModButton = Button(master, text="Edit Mods", height=1, width=6)
    ocvModButton.grid(row=326, column=62, columnspan=6)
    
    ocvModFrame = Frame(master, bd=2, relief=SUNKEN)
    ocvModFrame.grid_rowconfigure(0, weight=1)
    ocvModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(ocvModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(ocvModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    ocvModFrame.grid(row=326, column=68, columnspan=30)

    dcvModButton = Button(master, text="Edit Mods", height=1, width=6)
    dcvModButton.grid(row=326, column=99, columnspan=6)

    dcvModFrame = Frame(master, bd=2, relief=SUNKEN)
    dcvModFrame.grid_rowconfigure(0, weight=1)
    dcvModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(dcvModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(dcvModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    dcvModFrame.grid(row=326, column=105, columnspan=30)



    omcvText = Text(master, height=1, width = 31)
    omcvText.grid(row=395, column=62, columnspan=31, sticky=W)
    omcvText.insert(INSERT, "Offensive Mental Combat Value")
    omcvText.config(state=DISABLED)
    global omcvContent
    omcvContent = StringVar()
    omcvEntry = Entry(master, textvariable=omcvContent, width=5)
    omcvEntry.grid(row=395, column = 93, columnspan=5)
    omcvEntry.insert(0, "100")

    dmcvText = Text(master, height=1, width = 31)
    dmcvText.grid(row=395, column=99, columnspan=31, sticky=W)
    dmcvText.insert(INSERT,"Defensive Mental Combat Value")
    dmcvText.config(state=DISABLED)
    global dmcvContent
    dmcvContent = StringVar()
    dmcvEntry = Entry(master, textvariable=dmcvContent, width=5)
    dmcvEntry.grid(row=395, column = 130, columnspan=5)
    dmcvEntry.insert(0, "100")

    omcvModButton = Button(master, text="Edit Mods", height=1, width=6)
    omcvModButton.grid(row=396, column=62, columnspan=6)
    
    omcvModFrame = Frame(master, bd=2, relief=SUNKEN)
    omcvModFrame.grid_rowconfigure(0, weight=1)
    omcvModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(omcvModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(omcvModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    omcvModFrame.grid(row=396, column=68, columnspan=30)

    dmcvModButton = Button(master, text="Edit Mods", height=1, width=6)
    dmcvModButton.grid(row=396, column=99, columnspan=6)

    dmcvModFrame = Frame(master, bd=2, relief=SUNKEN)
    dmcvModFrame.grid_rowconfigure(0, weight=1)
    dmcvModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(dmcvModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(dmcvModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    dmcvModFrame.grid(row=396, column=105, columnspan=30)



    spdText = Text(master, height=1, width = 31)
    spdText.grid(row=535, column=62, columnspan=31, sticky=W)
    spdText.insert(INSERT, "Speed")
    spdText.config(state=DISABLED)
    global spdContent
    spdContent = StringVar()
    spdEntry = Entry(master, textvariable=spdContent, width=5)
    spdEntry.grid(row=535, column = 93, columnspan=5)
    spdEntry.insert(0, "100")

    spdModButton = Button(master, text="Edit Mods", height=1, width=6)
    spdModButton.grid(row=536, column=62, columnspan=6)
    
    spdModFrame = Frame(master, bd=2, relief=SUNKEN)
    spdModFrame.grid_rowconfigure(0, weight=1)
    spdModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(spdModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(spdModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    spdModFrame.grid(row=536, column=68, columnspan=30)



    pdText = Text(master, height=1, width = 31)
    pdText.grid(row=675, column=62, columnspan=31, sticky=W)
    pdText.insert(INSERT, "Physical Defense")
    pdText.config(state=DISABLED)
    global pdContent
    pdContent = StringVar()
    pdEntry = Entry(master, textvariable=pdContent, width=5)
    pdEntry.grid(row=675, column = 93, columnspan=5)
    pdEntry.insert(0, "100")

    edText = Text(master, height=1, width = 31)
    edText.grid(row=675, column=99, columnspan=31, sticky=W)
    edText.insert(INSERT,"Energy Defense")
    edText.config(state=DISABLED)
    global edContent
    edContent = StringVar()
    edEntry = Entry(master, textvariable=edContent, width=5)
    edEntry.grid(row=675, column = 130, columnspan=5)
    edEntry.insert(0, "100")

    pdModButton = Button(master, text="Edit Mods", height=1, width=6)
    pdModButton.grid(row=676, column=62, columnspan=6)
    
    pdModFrame = Frame(master, bd=2, relief=SUNKEN)
    pdModFrame.grid_rowconfigure(0, weight=1)
    pdModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(pdModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(pdModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    pdModFrame.grid(row=676, column=68, columnspan=30)

    edModButton = Button(master, text="Edit Mods", height=1, width=6)
    edModButton.grid(row=676, column=99, columnspan=6)

    edModFrame = Frame(master, bd=2, relief=SUNKEN)
    edModFrame.grid_rowconfigure(0, weight=1)
    edModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(edModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(edModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    edModFrame.grid(row=676, column=105, columnspan=30)



    recText = Text(master, height=1, width = 31)
    recText.grid(row=675, column=62, columnspan=31, sticky=W)
    recText.insert(INSERT, "Recovery")
    recText.config(state=DISABLED)
    global recContent
    recContent = StringVar()
    recEntry = Entry(master, textvariable=recContent, width=5)
    recEntry.grid(row=675, column = 93, columnspan=5)
    recEntry.insert(0, "100")

    endText = Text(master, height=1, width = 31)
    endText.grid(row=675, column=99, columnspan=31, sticky=W)
    endText.insert(INSERT,"Endurance")
    endText.config(state=DISABLED)
    global endContent
    endContent = StringVar()
    endEntry = Entry(master, textvariable=endContent, width=5)
    endEntry.grid(row=675, column = 130, columnspan=5)
    endEntry.insert(0, "100")

    recModButton = Button(master, text="Edit Mods", height=1, width=6)
    recModButton.grid(row=676, column=62, columnspan=6)
    
    recModFrame = Frame(master, bd=2, relief=SUNKEN)
    recModFrame.grid_rowconfigure(0, weight=1)
    recModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(recModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(recModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    recModFrame.grid(row=676, column=68, columnspan=30)

    endModButton = Button(master, text="Edit Mods", height=1, width=6)
    endModButton.grid(row=676, column=99, columnspan=6)

    endModFrame = Frame(master, bd=2, relief=SUNKEN)
    endModFrame.grid_rowconfigure(0, weight=1)
    endModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(endModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(endModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    endModFrame.grid(row=676, column=105, columnspan=30)


    bodyText = Text(master, height=1, width = 31)
    bodyText.grid(row=815, column=62, columnspan=31, sticky=W)
    bodyText.insert(INSERT, "Body Health")
    bodyText.config(state=DISABLED)
    global bodyContent
    bodyContent = StringVar()
    bodyEntry = Entry(master, textvariable=bodyContent, width=5)
    bodyEntry.grid(row=815, column = 93, columnspan=5)
    bodyEntry.insert(0, "100")

    stunText = Text(master, height=1, width = 31)
    stunText.grid(row=815, column=99, columnspan=31, sticky=W)
    stunText.insert(INSERT,"Stun Health")
    stunText.config(state=DISABLED)
    global stunContent
    stunContent = StringVar()
    stunEntry = Entry(master, textvariable=stunContent, width=5)
    stunEntry.grid(row=815, column = 130, columnspan=5)
    stunEntry.insert(0, "100")

    bodyModButton = Button(master, text="Edit Mods", height=1, width=6)
    bodyModButton.grid(row=816, column=62, columnspan=6)
    
    bodyModFrame = Frame(master, bd=2, relief=SUNKEN)
    bodyModFrame.grid_rowconfigure(0, weight=1)
    bodyModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(bodyModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(bodyModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    bodyModFrame.grid(row=816, column=68, columnspan=30)

    stunModButton = Button(master, text="Edit Mods", height=1, width=6)
    stunModButton.grid(row=816, column=99, columnspan=6)

    stunModFrame = Frame(master, bd=2, relief=SUNKEN)
    stunModFrame.grid_rowconfigure(0, weight=1)
    stunModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(stunModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(stunModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Sample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Poinnts)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    stunModFrame.grid(row=816, column=105, columnspan=30)

    submitButton = Button(master, text="Submit", command=lambda: retrieveCurrentValues("Characteristics"))
    submitButton.grid(row=940, column=62, columnspan=74)

    submitButton2 = Button(master, text="Submit", command=eraseCharDetailsPage)
    submitButton2.grid(row=941, column=62, columnspan=74)

    
def drawSkillsPage():
    global spacer0
    spacer0 = Text(master, height=1, width=2)
    spacer0.grid(row=45, column=61)
    spacer0.config(state=DISABLED)

    global strText
    global strEntry
    strText = Text(master, height=1, width = 31)
    strText.grid(row=45, column=62, columnspan=31, sticky=W)
    strText.insert(INSERT, "Mength")
    strText.config(state=DISABLED)
    global strContent
    strContent = StringVar()
    strEntry = Entry(master, textvariable=strContent, width=5)
    strEntry.grid(row=45, column = 93, columnspan=5)
    strEntry.insert(0, "200")

    global spacer1
    spacer1 = Text(master, height=1, width=9)
    spacer1.grid(row=45, column=98)
    spacer1.config(state=DISABLED)

    global dexText
    global dexEntry
    dexText = Text(master, height=1, width = 31)
    dexText.grid(row=45, column=99, columnspan=31, sticky=W)
    dexText.insert(INSERT,"Mexterity")
    dexText.config(state=DISABLED)
    global dexContent
    dexContent = StringVar()
    dexEntry = Entry(master, textvariable=dexContent, width=5)
    dexEntry.grid(row=45, column = 130, columnspan=5)
    dexEntry.insert(0, "200")

    global strModButton
    strModButton = Button(master, text="Mdit Mods", height=1, width=6)
    strModButton.grid(row=46, column=62, columnspan=6)
    
    global strModFrame
    strModFrame = Frame(master, bd=2, relief=SUNKEN)
    strModFrame.grid_rowconfigure(0, weight=1)
    strModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(strModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(strModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Mample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Points)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    strModFrame.grid(row=46, column=68, columnspan=30)

    global dexModButton
    dexModButton = Button(master, text="Mdit Mods", height=1, width=6)
    dexModButton.grid(row=46, column=99, columnspan=6)

    global dexModFrame
    dexModFrame = Frame(master, bd=2, relief=SUNKEN)
    dexModFrame.grid_rowconfigure(0, weight=1)
    dexModFrame.grid_columnconfigure(0, weight=1)
    yscrollbar = Scrollbar(dexModFrame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    text = Text(dexModFrame, wrap=WORD, bd=0, yscrollcommand=yscrollbar.set, height = 2, width = 30)
    text.insert(INSERT, "•Mample Modifier(1/4 Advantage) \n•Another Modifier(1/2 Limitation) \n•Yet Another Sample(+5 Points)")
    text.config(state=DISABLED)
    text.grid(row=0, column=0, sticky=N+S+E+W)
    yscrollbar.config(command=text.yview)
    dexModFrame.grid(row=46, column=105, columnspan=30)

    submitButton = Button(master, text="Submit", command=eraseSkillsPage)
    submitButton.grid(row=840, column=62, columnspan=74)

    submitButton2 = Button(master, text="Submit", command=drawSkillsPage)
    submitButton2.grid(row=940, column=62, columnspan=74)


def eraseSkillsPage():
    spacer0.grid_forget()
    
    strText.grid_forget()
    strEntry.grid_forget()
    
    spacer1.grid_forget()

    dexText.grid_forget()
    dexEntry.grid_forget()

    strModButton.grid_forget()
    strModFrame.grid_forget()

    dexModButton.grid_forget()
    dexModFrame.grid_forget()


    
drawCharacteritiPage()


mainloop()
