#!/usr/bin/python
#ws2812b_neopixel
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)
	
pixels[0] = (255, 0, 0)
sleep(1)
# https://www.thegeekpub.com/16187/controlling-ws2812b-leds-with-a-raspberry-pi/
# sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
# sudo pip3 install            adafruit-circuitpython-neopixel
# sudo pip install rpi_ws281x
# https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/
# https://core-electronics.com.au/guides/ws2812-addressable-leds-raspberry-pi-quickstart-guide/

# https://core-electronics.com.au/videos/how-to-use-addressable-rgb-ws2812b-led-strips-with-a-raspberry-pi-single-board-computer
# https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel

# https://core-electronics.com.au/videos/how-to-use-ws2812b-rgb-leds-with-raspberry-pi

"""
Vi skal huske/tale om disse dele:
hdmi_force_hotplug=1
hdmi_force_edid_audio=1

https://github.com/rpi-ws281x/rpi-ws281x-python/releases

"""
