#!/usr/bin/python
import pygame
import random
#import math
def rnd(a,b=0): 
  if b==0: b,a = a,0
  return random.randint(a,b)


pygame.init() # Initialize Pygame and create a window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
#window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
#surface = pygame.Surface((window_width, window_height)) # Create a new surface to draw on

"""
something about picking a random place and random color,
counting up for 5 seconds, and down for 5 seconds,
then looping again.
"""

tick = 0.1
time_delay = int(tick*1000) #50 # ms 100 #1s 5000 # 5 seconds

class Blob:
  def __init__(self): 
    self.duration_s = rnd(1,20) # fixme, make 1-2-4-8-16
    self.halfway = self.duration_s*0.5
    self.passed = 0 # better names?
    self.pos = (rnd(255),rnd(255))
    self.color1 = (rnd(255), rnd(255), rnd(255))  
  #
  def act(self): 
    self.plot()
    self.passed += tick
    return (self.passed >= self.duration_s)
  def plot(self): 
    unit = 1.0-(abs(self.halfway-self.passed)/self.halfway)
    r = unit
    color=(int(r*self.color1[0]),int(r*self.color1[1]),int(r*self.color1[2]))
    p = self.pos
    rect = pygame.Rect(p[0],p[1],5,5)
    window.fill(color,rect)
  #


#########
blobs= [Blob(),Blob(),Blob()]

def spawn(n):
  global blobs
  for i in range(1,n):
    blobs.append(Blob())

def drawStuff():   
  global blobs
  rr=rnd(100)
  print('drawStuff, len:', len(blobs))
  nextBlobs=[]
  for blob in blobs:
    done = blob.act()
    if not done:
      nextBlobs.append(blob)
      
  blobs = nextBlobs
  if rr <9 and len(blobs)<100: spawn(rnd(1,4))
  pygame.display.update() # Update the display


# idea - do 1 2 4 8 16,
# and make different colors differnt lifetimes.




##################################################################################
##################################################################################
##################################################################################
#
timer_event = pygame.USEREVENT + 1

def initTimer(): # https://stackoverflow.com/questions/64415642/how-to-create-timers-in-pygame-efficiently
  pygame.time.set_timer(timer_event, time_delay)
initTimer() #https://gamedevacademy.org/pygame-timer-tutorial-complete-guide/

def quit():
  pygame.quit()
  exit()

def doEvent(event):
  if event.type == pygame.QUIT: quit()
  if event.type == timer_event: drawStuff() 

def main(): # Wait for the user to close the window
  while True:
    for event in pygame.event.get(): doEvent(event)
main()
