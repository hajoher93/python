import pygame

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() // 2
        self.rect.bottom = screen.get_height() - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen.get_width():
            self.rect.x += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)