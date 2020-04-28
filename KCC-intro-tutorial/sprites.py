# pylint: disable=no-member
# pylint: disable=too-many-function-args
# Skeleton for a new project
import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# Useful colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup Asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

class Player(pygame.sprite.Sprite):
  # sprite for the player
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    # self.image = pygame.Surface((50, 50))
    # self.image.fill(GREEN) 
    self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
    self.image.set_colorkey(BLACK)
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH / 2, HEIGHT / 2)
    self.y_speed = 5
  
  def update(self):
    self.rect.x += 5
    self.rect.y += self.y_speed
    if self.rect.left > WIDTH:
      self.rect.right = 0
    if self.rect.bottom > HEIGHT - 100:
      self.y_speed = -5
    if self.rect.top < 200:
      self.y_speed = 5

# Initialise pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Setup Sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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