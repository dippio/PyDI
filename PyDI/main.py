# pydi v0.1
# simple cli program for playing midi instruments in the terminal
# main.py // the main program

from select import select                                                                                                # imports
import mido
import time
import textual
import deviceSelect as devSel
from deviceSelect import *
import notationConvert
from notationConvert import notationConverter, arithmeticSequence, tempNumber

i = 0                                                                                                                    #define some variables to avoid crashes
selectedDevice = 0
chromaticNote = 0
tempNumber = 27
noteArray = []  
output_port = mido.open_output()                                                                                                         

chromatic2 = ["C", "C♯", "D♭", "D", "D♯", "E♭", "E", "F", "F♯", "G♭", "G", "G♯", "A♭", "A", "A♯", "B♭", "B"]             # chromatic scale with flats and sharps seperated
chromaticScale = ["C", "D♭ / C♯", "D", "E♭ / D♯", "E", "F", "G♭ / F♯", "G", "A♭ / G♯", "A", "B♭ / A♯", "B"]              # chromatic scale with flats and sharps as same key

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
        if tempVelocity >= 1:
            if chromeTempNo == 13:
                chromeTempNo = 0
            else:
                arithmeticSequence(arithTempNo)
                if tempNote in noteArray:
                    chromaticNote = chromaticScale[chromeTempNo]
                    print(chromaticNote)
                    break
                else:
                    arithTempNo = arithTempNo + 1
                    chromeTempNo = chromeTempNo + 1
        else:
            break

selectMIDIDevice()

with mido.open_input(devSel.deviceNames[selectedDevice]) as port:                                                                                                                                           # if you see this that likely means a MIDI device isn't being detected by the program. please make sure a MIDI device is properly connected, and try again.
    for msg in port:
        output_port.send(msg)
        tempNote = msg.note
        tempVelocity = msg.velocity
        notationConverter()
        



