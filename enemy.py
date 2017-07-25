import pygame
from random import *


class SmallEnemy(pygame.sprite.Sprite):
    """docstring for SmallEnemy"""
    energy = 1

    def __init__(self, bg_size):
        super(SmallEnemy, self).__init__()

        self.image = pygame.image.load('images/enemy1.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy1_down1.png').convert_alpha(),
            pygame.image.load('images/enemy1_down2.png').convert_alpha(),
            pygame.image.load('images/enemy1_down3.png').convert_alpha(),
            pygame.image.load('images/enemy1_down4.png').convert_alpha()
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2
        self.reset()
        self.energy = SmallEnemy.energy
        self.hit = False
        

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        self.active = True
        self.energy = SmallEnemy.energy


class MidEnemy(pygame.sprite.Sprite):
    """docstring for MidEnemy"""

    energy = 8

    def __init__(self, bg_size):
        super(MidEnemy, self).__init__()

        self.image = pygame.image.load('images/enemy2.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy2_down1.png').convert_alpha(),
            pygame.image.load('images/enemy2_down2.png').convert_alpha(),
            pygame.image.load('images/enemy2_down3.png').convert_alpha(),
            pygame.image.load('images/enemy2_down4.png').convert_alpha()
            ])
        self.image_hit = pygame.image.load('images/enemy2_hit.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.reset()
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)
        self.active = True
        self.energy = MidEnemy.energy


class BigEnemy(pygame.sprite.Sprite):
    """docstring for BigEnemy"""
    energy = 20

    def __init__(self, bg_size):
        super(BigEnemy, self).__init__()

        self.image1 = pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('images/enemy3_n2.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy3_down1.png').convert_alpha(),
            pygame.image.load('images/enemy3_down2.png').convert_alpha(),
            pygame.image.load('images/enemy3_down3.png').convert_alpha(),
            pygame.image.load('images/enemy3_down4.png').convert_alpha(),
            pygame.image.load('images/enemy3_down5.png').convert_alpha(),
            pygame.image.load('images/enemy3_down6.png').convert_alpha()
            ])
        self.image_hit = pygame.image.load('images/enemy3_hit.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image1)
        self.appear = False
        self.reset()
        self.energy = BigEnemy.energy
        self.hit = False


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-20 * self.height, -10 * self.height) 
        self.active = True
        self.energy = BigEnemy.energy
