#!/usr/bin/python3

#mport Adafruit_CharLCD as LCD
import Adafruit_CharLCD as LCD
import time

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# TypeError: __init__() missing 8 required positional arguments: 'rs', 'en', 'd4', 'd5', 'd6', 'd7', 'cols', and 'lines'
#bob=LCD.Adafruit_CharLCD()

print('a')
#lcd=LCD.Adafruit_CharLCDPlate(address=0x20,busnum=1)
lcd = LCD.Adafruit_CharLCDBackpack() #address=0x20)

print('ba')

#bob=LCD.Adafruit_RGBCharLCD()

# Initialize the LCD using the pins
#lcd = LCD.Adafruit_CharLCDBackpack()

# Turn backlight on
print('ca')
lcd.set_backlight(0)
print('da')

# Print a two line message
print('ea')
lcd.message('Hello\nworld!')
print('fa')

# Wait 5 seconds
print('ga')
time.sleep(5.0)
print('ha')

# Demo showing the cursor.
print('ia')
lcd.clear()
print('ja')
lcd.show_cursor(True)
print('ka')
lcd.message('Show cursor')

print('a')
time.sleep(5.0)

# Demo showing the blinking cursor.
lcd.clear()
print('a')
lcd.blink(True)
print('a')
lcd.message('Blink cursor')
print('a')

time.sleep(5.0)
print('a')

# Stop blinking and showing cursor.
lcd.show_cursor(False)
print('a')
lcd.blink(False)
print('a')

# Demo scrolling message right/left.
lcd.clear()
print('a')
message = 'Scroll'
print('a')
lcd.message(message)
print('a')
for i in range(lcd_columns-len(message)):
    print('a')
    time.sleep(0.5)
    lcd.move_right()
    
print('a')
    
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()
    print('a')

print('a')
# Demo turning backlight off and on.

lcd.clear()
print('a')
lcd.message('Flash backlight\nin 5 seconds...')
print('a')
time.sleep(5.0)
print('a')
# Turn backlight off.
lcd.set_backlight(1)
print('a')
time.sleep(2.0)
print('a')
# Change message.
lcd.clear()
print('a')
lcd.message('Goodbye!')
print('a')
# Turn backlight on.
lcd.set_backlight(0)
print('a')
