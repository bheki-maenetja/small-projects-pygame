# pylint: disable=no-member
# pylint: disable=too-many-function-args
# pylint: disable=no-name-in-module
# Skeleton for a new project
import pygame
from random import randint, choice
from math import cos, sin, pi
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
    angle_deg = ((self.rot % 360) + 90) % 360
    angle_rad = (angle_deg / 180) * pi
    horizontal_vector = abs(8 * round(cos(angle_rad), 4))
    vertical_vector = abs(8 * round(sin(angle_rad), 4))
    print(round(sin(angle_rad), 4), round(cos(angle_rad), 4))
    if 0 <= angle_deg <= 90:
      self.rect.centerx += horizontal_vector
      self.rect.centery -= vertical_vector
    if 90 < angle_deg <= 180:
      self.rect.centerx -= horizontal_vector
      self.rect.centery -= vertical_vector
    if 180 < angle_deg <= 270:
      self.rect.centerx -= horizontal_vector
      self.rect.centery += vertical_vector
    if 270 < angle_deg <= 360:
      self.rect.centerx += horizontal_vector
      self.rect.centery += vertical_vector
    
    self.boundary_check()
  
  def boundary_check(self):
    if self.rect.top < 0 or self.rect.bottom > HEIGHT or self.rect.left < 0 or self.rect.right > WIDTH:
      self.kill()

class Alien(pygame.sprite.Sprite):
  def __init__(self):
    super(Alien, self).__init__()
    self.image = pygame.Surface((30, 30))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
    self.direction = choice(['left', 'right', 'top', 'bottom'])
    self.spawn()
  
  def spawn(self):
    if (self.direction == 'left'):
      x, y = randint(-100, -5), randint(0, HEIGHT)
    if (self.direction == 'right'):
      x, y = randint(WIDTH + 5, WIDTH + 100), randint(0, HEIGHT)
    if (self.direction == 'top'):
      x, y = randint(0, WIDTH), randint(-100, -5)
    if (self.direction == 'bottom'):
      x, y = randint(0, WIDTH), randint(HEIGHT + 5, HEIGHT + 100)
    self.rect.center = (x, y)
  
  def update(self):
    if (self.direction == 'left'):
      self.rect.centerx += 5
    if (self.direction == 'right'):
      self.rect.centerx -= 5
    if (self.direction == 'top'):
      self.rect.centery += 5
    if (self.direction == 'bottom'):
      self.rect.centery -= 5

player = Player()
all_sprites.add(player)

# Utility Functions
def spanw_aliens():
  for i in range(50):
    new_alien = Alien()
    all_sprites.add(new_alien)

spanw_aliens()

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