import pygame

class Bullet1(pygame.sprite.Sprite):
    """docstring for Bullet1"""
    def __init__(self, position):
        super(Bullet1, self).__init__()

        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

class Bullet2(pygame.sprite.Sprite):
    """docstring for Bullet2"""
    def __init__(self, position):
        super(Bullet2, self).__init__()

        self.image = pygame.image.load("images/bullet2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 14
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True