import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('assets/background.png')
        self.player = Player(self.screen)
        self.enemies = [Enemy(self.screen) for _ in range(5)]
        self.bullets = []
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.screen.blit(self.background, (0, 0))
        self.player.update()
        self.player.draw()
        self.update_bullets()
        self.update_enemies()
        pygame.display.flip()
        self.clock.tick(60)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
            bullet.draw()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()
            enemy.draw()

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.screen, self.player.rect.centerx, self.player.rect.top))
