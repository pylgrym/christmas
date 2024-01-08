#!/usr/bin/python
from sense_hat import SenseHat

def drawBlobs_PI(blobs):
  for blob in blobs:
    color = blob.calc_color()
    p = blob.pos
    #rect = pygame.Rect(p[0],p[1],5,5)
    #window.fill(color,rect)
    sense.set_pixel(p[0], p[1], color)
