# pylint: disable=no-member
# pylint: disable=too-many-function-args
# pylint: disable=no-name-in-module
# Skeleton for a new project
import pygame
from random import randint, choice
from math import cos, sin
from os import path

from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_SPACE,
  K_d,
  K_a
)

# Initialise pygame and create window
WIDTH = 600
HEIGHT = 600
FPS = 60

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

player_image = pygame.image.load(path.join(img_dir, 'playerShip1_blue.png')).convert()

# Setup Sprites
all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.org_image = player_image
    self.image = self.org_image.copy()
    self.rect = self.image.get_rect()
    self.rect.center = ((WIDTH / 2, HEIGHT / 2))
    self.rot = 0
  
  def update(self):
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
      self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
      self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
      self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
      self.rect.move_ip(5, 0)
    if pressed_keys[K_a]:
      self.rotate(5)
    if pressed_keys[K_d]:
      self.rotate(-5)
    
    self.boundary_check()
  
  def rotate(self, rotation):
    self.rot += rotation
    old_center = self.rect.center
    new_image = pygame.transform.rotozoom(self.org_image, self.rot, 1)
    self.image = new_image
    self.rect = self.image.get_rect()
    self.rect.center = old_center
    print(((self.rot % 360) + 90) % 360)
  
  def boundary_check(self):
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > HEIGHT:
      self.rect.bottom = HEIGHT
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > WIDTH:
      self.rect.right = WIDTH
  
  def fire_bullet(self):
    new_bullet = Bullet(self.rot, self.rect.centerx, self.rect.centery)
    all_sprites.add(new_bullet)

class Bullet(pygame.sprite.Sprite):
  def __init__(self, rotation, x, y):
    super(Bullet, self).__init__()
    self.org_image = pygame.Surface((5, 20))
    self.org_image.fill(WHITE)
    self.rot = rotation
    self.image = self.org_image.copy()
    self.image = pygame.transform.rotozoom(self.org_image, rotation, 1)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
  
  def update(self):
    angle = ((self.rot % 360) + 90) % 360
    if 0 <= angle <= 90:
      self.rect.centerx += 5 * abs(cos(angle))
      self.rect.centery -= 5 * abs(sin(angle))
    if 90 < angle <= 180:
      self.rect.centerx -= 5 * abs(cos(angle))
      self.rect.centery -= 5 * abs(sin(angle))
    if 180 < angle <= 270:
      self.rect.centerx -= 5 * abs(cos(angle))
      self.rect.centery += 5 * abs(sin(angle))
    if 270 < angle <= 360:
      self.rect.centerx += 5 * abs(cos(angle))
      self.rect.centery += 5 * abs(sin(angle))
    
    self.boundary_check()
  
  def boundary_check(self):
    if self.rect.top < 0 or self.rect.bottom > HEIGHT or self.rect.left < 0 or self.rect.right > WIDTH:
      self.kill()

player = Player()

all_sprites.add(player)

# Game loop
running = True

while running:
  # Process input (events)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # check for closing the window
      running = False
    if event.type == pygame.KEYDOWN and event.key == K_SPACE:
      player.fire_bullet()

  # Update
  all_sprites.update()
  
  # Draw / render
  screen.fill(BLACK)
  all_sprites.draw(screen)

  # AFTER drawing everything, flip the display
  pygame.display.flip()

  # Keep game loop running at given FPS
  clock.tick(FPS)