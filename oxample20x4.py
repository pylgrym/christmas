#!/usr/bin/python3

import busio
import board
import time
import RPi.GPIO as GPIO
from PCF8574.lcd import LCD
from PCF8574.pcf8574 import PCF8574

# GPIO pins of the buttons
S1 = 4
S2 = 16
S3 = 10
S4 = 9
inputs = [S1, S2, S3, S4]
GPIO.setmode(GPIO.BCM)


def do1():
    print('do1')
def do2():
    print('do2')
def do3():
    print('do3')
def do4():
    print('do4')

def waitLoop():
    print('waitLoop starting')
    i=0
    while True:
        print(i); i+=1
        time.sleep(0.2)

def my_callback(ch):
    #print('Callback, channel:', ch)
    if ch==S1: do1()
    if ch==S2: do2()
    if ch==S3: do3()
    if ch==S4: do4()

# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    
# setting up buttons as inputs
# print(GPIO.__file__)
# print(dir(GPIO))
# help('RPi.GPIO')
for switch in inputs:
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #    
    GPIO.add_event_detect(switch, GPIO.RISING, bouncetime=200)
    GPIO.add_event_callback(switch, my_callback) #, bouncetime=200)



# set up lcd
lcd = LCD(PCF8574(busio.I2C(board.SCL, board.SDA),0x27), num_rows=4, num_cols=20)
lcd.print("Press a button!")

waitLoop()



def checkSwitches():
    #Check status of all four switches on the LCD board
    val1 = not GPIO.input(S1)
    val2 = not GPIO.input(S2)
    val3 = not GPIO.input(S3)
    val4 = not GPIO.input(S4)
    if val1 == GPIO.HIGH:
        return "S1"
    elif val2 == GPIO.HIGH:
        return "S2"
    elif val3 == GPIO.HIGH:
        return "S3"
    elif val4 == GPIO.HIGH:
        return "S4"
    return "0"


try:
    lcd.print("Press a button!")
    column = 0
    while(True):
        value = checkSwitches()
        # nothing is pressed
        if value == "0":
            continue

        if column == 0:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("You pressed "+value+"!")
            column += 1
        elif column == 1:
            lcd.set_cursor_pos(1, 0)
            lcd.print("You pressed "+value+"!")
            column += 1
        elif column == 2:
            lcd.set_cursor_pos(2, 0)
            lcd.print("You pressed "+value+"!")
            column += 1
        elif column == 3:
            lcd.set_cursor_pos(3, 0)
            lcd.print("You pressed "+value+"!")
            column -= 3
        time.sleep(1)
except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()
