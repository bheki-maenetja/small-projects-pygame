# pylint: disable=no-member
# pylint: disable=too-many-function-args
# Skeleton for a new project
import pygame
import random
from os import path
from math import sqrt

# INITIALISE PYGAME AND CREATE WINDOW
WIDTH = 360
HEIGHT = 480
FPS = 60

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

# GAME VARIABLES
x = 80
y = 80
dx = 10
dy = 10
score = 0
player_x = 0
player_y = 0

# TEXT
heading_font = pygame.font.Font(None, 48)
heading_text = heading_font.render("BOUNCY BALL GAME", 1, BLACK)

# UTILITY FUNCTIONS
def get_distance(first_coords, second_coords, r):
  d = sqrt((first_coords[0] - second_coords[0])**2 + (first_coords[1] - second_coords[1])**2)
  if d < r: return True

def update_score(surf, score):
  score_font = pygame.font.Font(None, 24)
  score_text = score_font.render(f"Score: {score}", 1, BLACK)
  surf.blit(score_text, (150, 45))

# GAME LOOP
running = True

while running:
  # Process Input (events)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # check for closing the window
      running = False
    if event.type == pygame.MOUSEMOTION:
      player_x, player_y = event.pos[0], event.pos[1]

  # Update
  all_sprites.update()
  x += dx
  y += dy

  if x + 25 > WIDTH or x - 25 < 0:
    dx = -dx
  if y + 25 > HEIGHT or y - 25 < 0:
    dy = -dy

  if get_distance((player_x, player_y), (x,y), 20): score += 5
  # Draw / Render
  screen.fill(YELLOW)
  all_sprites.draw(screen)
  pygame.draw.circle(screen, RED, (x,y), 25)
  pygame.draw.circle(screen, BLUE, (player_x, player_y), 20)
  screen.blit(heading_text, (5, 10))
  update_score(screen, score)

  # AFTER Drawing Everything, Flip the Display
  pygame.display.flip()

  # Keep Game Loop Running at Given FPS
  clock.tick(FPS)