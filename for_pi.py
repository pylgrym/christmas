#!/usr/bin/python
from sense_hat import SenseHat
from blob5 import updateBlobs #Blob5 as Blob
import time

tick_s = 0.1

def drawBlobs_PI(blobs):
  for blob in blobs:
    color = blob.calc_color()
    p = blob.pos
    #rect = pygame.Rect(p[0],p[1],5,5)
    #window.fill(color,rect)
    print('color:', color)
    SenseHat.set_pixel(p[0], p[1], color)


while True: #for i in range(1,100):
  blobs = updateBlobs(tick_s)  
  drawBlobs_PI(blobs)
  time.sleep(0.1)

