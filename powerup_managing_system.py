import pygame
import powerups

class powerup_manager():
    def __init__(self, screen, player, hider):
        self.screen = screen
        self.powerup = []
        self.player = player
        self.seeker = hider
        self.powerup.append(powerups.speed_boost())
        self.powerup.append(powerups.trap())

    def draw_powerups(self):
        for i in self.powerup:
            i.draw(self.screen)

    def collide_powerups(self):
        for i in self.powerup:
            i.collisions(self.player)
    
    def powerup_updates(self):
        for i in self.powerup:
            if i.name == "speed":
                i.update(self.player)
                if i.effect_dur == True:
                    self.powerup.remove(i)
            if i.name == "trap":
                i.update(self.player, self.seeker)

    def update_powerups(self):
        self.draw_powerups()
        self.collide_powerups()
        self.powerup_updates()