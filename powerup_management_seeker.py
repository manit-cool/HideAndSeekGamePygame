import pygame
import powerups

class powerup_manager():
    def __init__(self, screen, player):
        self.screen = screen
        self.powerup = []
        self.player = player
        self.powerup.append(powerups.speed_boost())
        self.powerup.append(powerups.phase_through_walls())
        self.powerup.append(powerups.barricade())

    def draw_powerups(self):
        for i in self.powerup:
            i.draw(self.screen)

    def collide_powerups(self, obstacles):
        for i in self.powerup:
            if i.name == "barricade":
                i.collision(self.player, obstacles)
            else:
                i.collisions(self.player)

    def powerup_updates(self):
        for i in self.powerup:
            if i.name == "speed" or  i.name == "phase":
                i.update(self.player)
                if i.effect_dur == True:
                    self.powerup.remove(i)

    def update_powerups(self, obstacles):
        self.draw_powerups()
        self.collide_powerups(obstacles)
        self.powerup_updates()