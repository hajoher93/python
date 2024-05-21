import pygame
import random

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('assets/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(-150, -100)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen.get_height():
            self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
            self.rect.y = random.randint(-150, -100)

    def draw(self):
        self.screen.blit(self.image, self.rect)