# pydi v0.1
# simple cli program for playing midi instruments in the terminal
# notationConvert.py // functions for converting mido data into standard music notation

chromatic2 = ["C", "C♯", "D♭", "D", "D♯", "E♭", "E", "F", "F♯", "G♭", "G", "G♯", "A♭", "A", "A♯", "B♭", "B"]             # chromatic scale with flats and sharps seperated
chromaticScale = ["C", "D♭ / C♯", "D", "E♭ / D♯", "E", "F", "G♭ / F♯", "G", "A♭ / G♯", "A", "B♭ / A♯", "B"]              # chromatic scale with flats and sharps as same key

chromaticNote = 0
tempNumber = 27
i = 0
noteArray = []  

def arithmeticSequence(delta):                                                                                          # mfw i need arithmetic mathematics type shit to convert a number to a letter
    global noteArray
    noteArray = []  
    i = 0                                                         
    x = 1
    init = 12
    while i <= 128:
        noteSequence = delta + (init * x)
        noteArray.append(noteSequence)
        x = x + 1
        i = i + init


def notationConverter():
    arithTempNo = 12
    chromeTempNo = 0
    while arithTempNo <= 128:
        if chromeTempNo == 13:
            chromeTempNo = 0
        else:
            arithmeticSequence(arithTempNo)
            if tempNumber in noteArray:
                chromaticNote = chromaticScale[chromeTempNo]
                print(chromaticNote)
                break
            else:
                arithTempNo = arithTempNo + 1
                chromeTempNo = chromeTempNo + 1