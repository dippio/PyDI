# pydi v0.1
# simple cli program for playing midi instruments in the terminal
# deviceSelect.py // define function for selecting MIDI devices

import mido
deviceNames = mido.get_input_names()

def selectMIDIDevice():
    i = 0
    selectedDevice = 0  
    for MIDIINPUTDEVICE in deviceNames:
        i = i + 1
        if i == 0:                                                                                                              # might not work properly bc mido generally causes an
            print("No MIDI devices are connected / detected. Make sure the device is plugged in proerply, and try again. ")     # out of range error when 0 devices are connected
            selectedDevice = 1000000                                                                                            # theres prolly a way around that but i'm
            input(" ")                                                                                                          # not smart enough to figure it out lol
            exit()
        elif i == 1:
            print("Using MIDI device 1: ", MIDIINPUTDEVICE, ", as no other devices are connected.")
            selectedDevice = 0
        else:
            print('Currently connected MIDI devices: ')                                                                         # i don't have a 2nd MIDI cable to confirm whether
            print(i, ": ", MIDIINPUTDEVICE)                                                                                     # this actually works properly or not
            selectedDevice = input("What  device would you like to use? (1 - ", i, ", press enter for default): ")
