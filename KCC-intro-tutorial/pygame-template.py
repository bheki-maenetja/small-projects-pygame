# pylint: disable=no-member
# Skeleton for a new project
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Useful colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialise pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game loop
running = True

while running:
  # Process input (events)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # check for closing the window
      running = False

  # Update
  
  # Draw / render
  screen.fill(BLUE)

  # AFTER drawing everything, flip the display
  pygame.display.flip()

  # Keep game loop running at given FPS
  clock.tick(FPS)