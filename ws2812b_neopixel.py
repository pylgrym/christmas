#!/usr/bin/python
#ws2812b_neopixel
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)
	
pixels[0] = (255, 0, 0)
sleep(1)
# https://www.thegeekpub.com/16187/controlling-ws2812b-leds-with-a-raspberry-pi/
