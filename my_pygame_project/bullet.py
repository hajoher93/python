import pygame

class Bullet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load('assets/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def off_screen(self):
        return self.rect.bottom < 0