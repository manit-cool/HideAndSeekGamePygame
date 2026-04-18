import pygame
import random

class wall():
    def __init__(self):
        self.x = random.randint(250, 1030)
        self.y = random.randint(250, 470)
        self.rect = pygame.Rect(self.x, self.y, random.randint(100, 250), random.randint(100, 250))

    def draw(self, screen):
        pygame.draw.rect(screen,(205, 247, 213),self.rect)

    def un_stuck(self, collidables):
        for i in collidables:
            while self.rect.colliderect(i.rect):
                if i.name == 1 and i.phase == True:
                    break
                
                else:
                    overlap_left   = i.rect.right - self.rect.left
                    overlap_right  = self.rect.right - i.rect.left
                    overlap_top    = i.rect.bottom - self.rect.top
                    overlap_bottom = self.rect.bottom - i.rect.top

                    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                    if min_overlap == overlap_left:
                        i.rect.x -= overlap_left 
                        if (i.name == 1 or i.name == 0):
                            i.player_pos.x = i.rect.x

                    elif min_overlap == overlap_right:
                        i.rect.x += overlap_right 
                        if (i.name == 1 or i.name == 0):
                            i.player_pos.x = i.rect.x
                    
                    elif min_overlap == overlap_top:
                        i.rect.y -= overlap_top 
                        if (i.name == 1 or i.name == 0):
                            i.player_pos.y = i.rect.y

                    elif min_overlap == overlap_bottom:
                        i.rect.y += overlap_bottom
                        if (i.name == 1 or i.name == 0):
                            i.player_pos.y = i.rect.y

    def update(self, screen, collidables):
        self.draw(screen) 
        self.un_stuck(collidables)
    