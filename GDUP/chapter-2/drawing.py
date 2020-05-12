# pylint: disable=no-member
# pylint: disable=too-many-function-args
# Skeleton for a new project
import pygame
import random
from os import path
from math import radians

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

# Load all sprite images
img_dir = path.join(path.dirname(__file__), 'img')

# Setup Sprites
all_sprites = pygame.sprite.Group()

# Text
font = pygame.font.Font(None, 36)
text = font.render("Hi there!", 1, TEAL)

# GAME LOOP
running = True

while running:
  # Process input (events)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # check for closing the window
      running = False

  # UPDATE
  all_sprites.update()
  
  # DRAW / RENDER
  screen.fill(WHITE)
  ## Drawing Lined Paper
  # y = 20
  # for n in range(0, 27):
  #   for x in range(0, WIDTH):
  #     screen.set_at((x, y), BLUE)
  #   y += 20
  
  # for y in range (0, HEIGHT):
  #   screen.set_at((25, y), RED)

  ## Drawing a colour gradient
  # blue = 0
  # delta = 255.0/HEIGHT
  # for y in range (0, HEIGHT):
  #   yy = HEIGHT-y
  #   c = (40, 40, blue)
  #   for x in range(0, WIDTH):
  #     screen.set_at((x, y), c) 
  #   blue = blue + delta
  # all_sprites.draw(screen)

  ## Drawing Lined Paper
  # y = 20
  # for n in range(0, 27):
  #   pygame.draw.line(screen, BLUE, (0, y), (WIDTH, y))
  #   y += 20
  
  # pygame.draw.line(screen, RED, (25, 0), (25, HEIGHT))

  # # Drawing polygons
  # pygame.draw.rect(screen, RED, (100, 100, 200, 200), 5)
  # pygame.draw.ellipse(screen, SIENNA, (50, 10, 150, 50), 5)
  # pygame.draw.circle(screen, MAGENTA, (200, 300), 120)

  # Drawing arcs
  pygame.draw.arc(screen, BLUE, (100, 100, 100, 50),0, radians(270))

  # Drawing text
  screen.blit(text, (WIDTH / 2, HEIGHT / 2))

  # AFTER drawing everything, flip the display
  pygame.display.flip()

  # Keep game loop running at given FPS
  clock.tick(FPS)