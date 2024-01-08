#!/usr/bin/python
import pygame
import random

# Initialize Pygame and create a window
pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

# Create a new surface to draw on
surface = pygame.Surface((window_width, window_height))

# Set a pixel at coordinates (x, y) with a specified color

for i in range(1,1000):
    x, y = 100, 200
    x+= random.randint(10,90)
    y+= random.randint(10,90)
    color = (255, 0, 0)  # Red
    surface.set_at((x, y), color)

# Blit the surface onto the window
window.blit(surface, (0, 0))

# Update the display
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
