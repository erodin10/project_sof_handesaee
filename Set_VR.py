import time
import binascii
try:
    import serial
except:
    print("Serial not installed")
from easygui import *
import VR_controller as VR

def main():
    vr = VR.VR_controller()
    message = "Select command for VR Module"
    title = "VR COMMAND"
    choices = list(vr.commands.keys())
 #   print(choices)
    command = choicebox(message, title, choices)
    print(command + ":", binascii.hexlify(vr.commands[command]))


if __name__ == "__main__":
    main()