import pygame
import random

class phase_through_walls():
    def __init__(self):
        self.name = "phase"
        self.rect = pygame.Rect(random.randint(0,1255), random.randint(0,695), 25, 25)
        self.phase = False
        self.timer = 0
        self.collected = False
        self.destruct = False

    def draw(self, screen):
        pygame.draw.rect(screen, (159, 133, 255), self.rect)
    
    def collisions(self, player):
        if pygame.Rect.colliderect(self.rect, player):
            player.rect.x = 1230
            self.collected = True
            player.phase = True

    def timer_start(self):
        self.timer += 1

    def effect_dur(self, player):
        pass