#!/usr/bin/python

print('hi')
import Adafruit_CharLCD as LCD


lcd_columns=16
lcd_rows=2
lcd = LCD.Adafruit_CharLCDBackpack(address=0x20)
lcd.set_backlight(0)
lcd.set_backlight(1)

# sudo i2cdetect -y 1

