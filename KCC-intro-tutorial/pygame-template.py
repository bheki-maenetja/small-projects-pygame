# pylint: disable=no-member
# pylint: disable=too-many-function-args
# Skeleton for a new project
import pygame
import random
from os import path

# Initialise pygame and create window
WIDTH = 360
HEIGHT = 480
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Useful colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load all sprite images
img_dir = path.join(path.dirname(__file__), 'img')

# Setup Sprites
all_sprites = pygame.sprite.Group()

# Game loop
running = True

while running:
  # Process input (events)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # check for closing the window
      running = False

  # Update
  all_sprites.update()
  
  # Draw / render
  screen.fill(BLUE)
  all_sprites.draw(screen)

  # AFTER drawing everything, flip the display
  pygame.display.flip()

  # Keep game loop running at given FPS
  clock.tick(FPS)