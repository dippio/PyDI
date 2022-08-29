# pydi v0.1
# simple cli program for playing midi instruments in the terminal
# main.py // the main program

# imports
from select import select
import mido
import time
import textual
import deviceSelect as devSel
from deviceSelect import *

#define some variables to avoid crashes
i = 0
selectedDevice = 0
output_port = mido.open_output()                                                                                                         

selectMIDIDevice()

with mido.open_input(devSel.deviceNames[selectedDevice]) as port:                                                                 # main mido function to actually play notes n stuff
    for msg in port:
        output_port.send(msg)
        print(msg)


