#!/usr/bin/python
import pygame
import random

# Initialize Pygame and create a window
pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
#window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)


def rnd(a,b=0): 
  if b==0: b,a = a,0
  return random.randint(a,b)

surface = pygame.Surface((window_width, window_height)) # Create a new surface to draw on

"""
something about picking a random place and random color,
counting up for 5 seconds, and down for 5 seconds,
then looping again.
"""

dir = 1
step = 1
step_max = 20
step_min = 1
pos=()
color1 = (rnd(255), rnd(255), rnd(255))  # Red

def reset():
  print('reset')
  global step,dir,pos,color1
  dir = 1
  step = 1
  pos = (rnd(255),rnd(255))
  color1 = (rnd(255), rnd(255), rnd(255))  # Red
  print('color1:', color1)
reset()

def plot(p,step):
  r = 1.0*step/step_max
  color=(int(r*color1[0]),int(r*color1[1]),int(r*color1[2]))
  rect = pygame.Rect(p[0],p[1],5,5)
  window.fill(color,rect)

def drawStuff(): 
  global step,dir,pos
  step += dir
  print(step,dir)
  if step >= step_max : dir = -1
  if step <= step_min: 
    reset()
    return # or globals will mess us up.
  plot(pos,step)
  #window.blit(surface, (0, 0)) # Blit the surface onto the window
  #window.set_at
  pygame.display.update() # Update the display

timer_event = pygame.USEREVENT + 1

def initTimer(): # https://stackoverflow.com/questions/64415642/how-to-create-timers-in-pygame-efficiently
  time_delay = 50 #100 #1s 5000 # 5 seconds
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
