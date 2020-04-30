# pylint: disable=too-many-function-args
# pylint: disable=no-member
import pygame
import random
from os import path

# Initialise pygame and create window
WIDTH = 480
HEIGHT = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot 'em Up!!!")
clock = pygame.time.Clock()

# Useful colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load all sprite images
img_dir = path.join(path.dirname(__file__), 'img')

background = pygame.image.load(path.join(img_dir, "blue.jpg")).convert()
background_rect = background.get_rect()

player_img = pygame.image.load(path.join(img_dir, 'playerShip2_blue.png')).convert()
laser_img = pygame.image.load(path.join(img_dir, 'laserGreen06.png')).convert()
meteor_img = pygame.image.load(path.join(img_dir, 'meteorBrown_med3.png')).convert()

# Setup Sprites
class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    # self.image = pygame.Surface((50, 40))
    # self.image.fill(BLUE)
    self.image = pygame.transform.scale(player_img, (60, 40))
    self.image.set_colorkey(BLACK)
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT - 10
    self.speedX = 0
  
  def update(self):
    self.speedX = 0
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_LEFT]:
      self.speedX = -5
    if keystate[pygame.K_RIGHT]:
      self.speedX = 5
    
    self.rect.x += self.speedX

    if self.rect.right > WIDTH:
      self.rect.right = WIDTH
    if self.rect.left < 0:
      self.rect.left = 0
  
  def shoot(self):
    bullet = Bullet(self.rect.centerx, self.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    # self.image = pygame.Surface((30, 40))
    # self.image.fill(RED)
    self.image = meteor_img
    self.image.set_colorkey(BLACK)
    self.rect = self.image.get_rect()
    self.rect.x = random.randint(0, WIDTH - self.rect.width)
    self.rect.y = random.randint(-100, -40)
    self.speedY = random.randint(1, 10)
    self.speedX = random.randint(-5, 5)
  
  def update(self):
    self.rect.y += self.speedY
    self.rect.x += self.speedX
    if self.rect.top > HEIGHT + 10 or self.rect.right > WIDTH + 20 or self.rect.left < 0:
      self.rect.x = random.randint(0, WIDTH - self.rect.width)
      self.rect.y = random.randint(-100, -40)
      self.speedY = random.randint(1, 10)

class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    # self.image = pygame.Surface((10, 20))
    # self.image.fill(WHITE)
    self.image = laser_img
    self.rect = self.image.get_rect()
    self.rect.bottom = y
    self.rect.centerx = x
    self.speedY = -10
  
  def update(self):
    self.rect.y += self.speedY
    if self.rect.bottom < 0:
      self.kill()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()

all_sprites.add(player)
for i in range(10):
  m = Mob()
  all_sprites.add(m)
  mobs.add(m)

# Game loop
running = True

while running:
  # Process input (events)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # check for closing the window
      running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      player.shoot()

  # Update
  all_sprites.update()

  bullet_hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
  for hit in bullet_hits:
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

  hits = pygame.sprite.spritecollide(player, mobs, False)
  if hits:
    running = False
    
  # Draw / render
  screen.fill(BLACK)
  screen.blit(background, background_rect)
  all_sprites.draw(screen)

  # AFTER drawing everything, flip the display
  pygame.display.flip()

  # Keep game loop running at given FPS
  clock.tick(FPS)