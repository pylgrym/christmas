import pygame
from blob5 import updateBlobs #Blob5 as Blob

pygame.init() # Initialize Pygame and create a window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

tick_s = 0.1
time_delay = int(tick_s*1000) #50 # ms 100 #1s 5000 # 5 seconds

#########
def drawBlobs(blobs):
  for blob in blobs:
    color = blob.calc_color()
    p = blob.pos
    dim=5
    rect = pygame.Rect(p[0]*dim,p[1]*dim,dim,dim)
    window.fill(color,rect)

def drawStuff():   
  blobs = updateBlobs(tick_s)
  drawBlobs(blobs)
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
