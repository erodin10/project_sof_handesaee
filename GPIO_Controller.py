import RPi.GPIO as GPIO
import time



"""
Decode the voice recognizer

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
    *



"""

global group
global sentence

def one(channel):
    global group
    if group == [0,1]:
        sentence += "Call Room"
    elif group == [1,0]:
        sentence += "Answer Call"
    elif group == [1,1]:
        sentence += ""
def two(channel):
    global group
    if group == [0,1]:
        sentence += "Unlock"
    elif group == [1,0]:
        sentence += "Kill"
    elif group == [1,1]:
        pass
def three(channel):
    global group
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

def call_group(group):
    GPIO.output(36, group[0]) #higher order
    GPIO.output(37, group[1]) #lower order

    time.sleep(0.1)

    GPIO.output(36, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)


def main():
    global group
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)

    group = [0, 1]

    call_group(group)
    sentence = ""

    funcs = [one, two, three, four, five] #list of functions for each interrupt



    while 1:
        time.sleep(1)
        print(sentence)

    GPIO.cleanup()


if __name__ == "__main__":
    main()

