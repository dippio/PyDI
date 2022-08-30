# pydi v0.1
# simple cli program for playing midi instruments in the terminal
# main.py // the main program

from select import select                                                                                                         # imports
import mido
import time
import textual
import deviceSelect as devSel
from deviceSelect import *
import notationConvert
from notationConvert import notationConverter, arithmeticSequence, tempNumber

i = 0                                                                                                                             #define some variables to avoid crashes
selectedDevice = 0
output_port = mido.open_output()                                                                                                         

selectMIDIDevice()

arithmeticSequence(15)

with mido.open_input(devSel.deviceNames[selectedDevice]) as port:                                                                 # main mido function to actually play notes n stuff
    for msg in port:
        output_port.send(msg)
        tempNumber = msg.note
        notationConverter()
        



