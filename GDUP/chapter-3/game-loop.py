# pylint: disable=no-member
# pylint: disable=too-many-function-args
# Skeleton for a new project
import pygame
import random
from os import path

# INITIALISE PYGAME AND CREATE WINDOW
WIDTH = 360
HEIGHT = 480
FPS = 60
x = 80
y = 80
dx = 10
dy = 10

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# USEFUL COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
MAGENTA = (255, 0, 255)
OLIVE = (128, 128, 0)
KHAKI = (240, 230, 140)
TEAL = (0, 128, 128)
SIENNA = (160, 83, 45)
TAN = (210, 180, 140)
INDIGO = (75, 0, 130)

# LOAD ALL SPRITE IMAGES
img_dir = path.join(path.dirname(__file__), 'img')

# SETUP SPRITES
all_sprites = pygame.sprite.Group()

# GAME LOOP
running = True
new_colour = YELLOW
while running:
  # Process Input (events)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # check for closing the window
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if 10 <= event.pos[0] <= 70 and 10 <= event.pos[1] <= 50:
        new_colour = random.choice((BLUE, GREEN, YELLOW, SIENNA, ORANGE, TAN, INDIGO))

  # Update
  all_sprites.update()
  x += dx
  y += dy

  if x + 25 > WIDTH or x - 25 < 0:
    dx = -dx
  if y + 25 > HEIGHT or y - 25 < 0:
    dy = -dy
  
  # Draw / Render
  screen.fill(new_colour)
  all_sprites.draw(screen)
  pygame.draw.circle(screen, TEAL, (x,y), 25)
  pygame.draw.rect(screen, MAGENTA, (10, 10, 60, 40))

  # AFTER Drawing Everything, Flip the Display
  pygame.display.flip()

  # Keep Game Loop Running at Given FPS
  clock.tick(FPS)