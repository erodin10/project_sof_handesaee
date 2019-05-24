import RPi.GPIO as GPIO
import time



"""
Decode the voice recognizer

VR Module should be working in pulse mode(Negative pulse).

Group 1 i.e. [0,1]:
    *   Call
    *   Unlock
    *   Bolt
    *   One
    *   Two

Group 2 i.e. [1,0]:
    *   Answer
    *   Kill
    *   Reject
    *   Bolt
    *   Unlock

Group 3 i.e. [1,1]:
    *NOT USED IN THIS PROJECT



"""

global group #Holds CURRENT group number
global sentence #Holds Sentence recognized from module


"""
Each function should be called when interrupted by VR Module's GPIO corresponding to the name of the function.
Eg. if GPIO 1 goes low, then function one() gets called etc. etc.
"""
def one(channel):
    if group == [0,1]:
        sentence += "Call Room"
    elif group == [1,0]:
        sentence += "Answer Call"
    elif group == [1,1]:
        pass
def two(channel):
    if group == [0,1]:
        sentence += "Unlock"
    elif group == [1,0]:
        sentence += "Kill"
    elif group == [1,1]:
        pass
def three(channel):
    if group == [0,1]:
        sentence+="Bolt"
    elif group == [1,0]:
        sentence+="Reject"
    elif group == [1,1]:
        pass
def four(channel):
    if group == [0,1]:
        sentence +="One"
    elif group == [1,0]:
        sentence +="Bolt"
    elif group == [1,1]:
        pass
def five(channel):
    if group == [0,1]:
        sentence +="Two"
    elif group == [1,0]:
        sentence += "Unlock"
    elif group == [1,1]:
        pass


"""
Import different groups for Voice recognition.

parameter:
  Group 1: [0,1]
    "   2: [1,0]
    "   3: [1,1]
  
"""
def call_group(group):
    GPIO.output(36, group[0]) #higher order
    GPIO.output(37, group[1]) #lower order

    time.sleep(0.1)

    GPIO.output(36, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)


def main():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)

    group = [0, 1]

    call_group(group)
    sentence = ""

    funcs = [one, two, three, four, five] #list of functions for each interrupt

    for count,pin in enumerate([29, 31, 32, 33, 35]): #Asign the correct interrupt function to RBPi's corresponding GPIO's(in the list)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #in pull up because RS232 is '1' when idle
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=funcs[count]) #assign function to pin event


    while 1:
        time.sleep(1)
        print(sentence)

    GPIO.cleanup()


if __name__ == "__main__":
    main()

