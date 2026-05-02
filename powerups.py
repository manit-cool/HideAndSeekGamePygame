import pygame
import random
import obstacles

class speed_boost():
    def __init__(self):
        self.speed_boost_applied = 2.24
        self.rect = pygame.Rect(random.randint(0,1255), random.randint(0,695), 25, 25)
        self.name = "speed"
        self.collected = False
        self.timer = 0

        self.destruct = False

    def draw(self, screen):
        pygame.draw.rect(screen, (252, 186, 3), self.rect)
    
    def collisions(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            player.speed = self.speed_boost_applied
            self.rect.x = 1300
            self.collected = True
    
    def timer_start(self):
        self.timer += 1

    def effect_dur(self, player):
        if self.timer >= 360:
            player.speed = 1.5
            return True
        return False

    def update(self, player):
        if self.collected:
            self.timer_start() 
            self.effect_dur(player)

class trap():
    def __init__(self):
        self.name = "trap"
        self.rect = pygame.Rect(random.randint(0,1255), random.randint(0,695), 25, 25)
        self.trapped = False

        self.timer = 0
        self.can_place = False
        self.in_action = False
        self.glue_rect = pygame.Rect(1300, 1300, 25, 25)
        self.destruct = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, (173, 240, 255), self.rect)
        if self.in_action:
            pygame.draw.rect(screen, (177, 195, 196), self.glue_rect)

    def collisions(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            print("oh yeaaa i'm so kewl :D")
            self.can_place = True
            self.rect.x = 1300
    
    def glue_collision(self, enemy):
        if pygame.Rect.colliderect(self.glue_rect, enemy.rect):
            enemy.speed = 0
            self.glue_rect.x = 1300
            self.trapped = True

    def timer_start(self):
        self.timer += 1

    def effect_dur(self, enemy):
        if self.timer >= 360:
            enemy.speed = 1.75
            return True
        return False
    
    def glue_place(self, player):
        keys = pygame.key.get_pressed()
        if self.can_place & keys[pygame.K_SPACE]:
            self.glue_rect.x = player.rect.x
            self.glue_rect.y = player.rect.y
            self.in_action = True
            self.can_place = False

    def update(self, player, enemy_rect):
        self.glue_place(player)
        self.glue_collision(enemy_rect)

        if self.trapped:
            self.timer_start()
            self.effect_dur(enemy_rect)
        if self.effect_dur(enemy_rect):
            self.glue_rect.x = 1300
        
        return True
    
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
            self.rect.x = 1300
            self.collected = True
            player.phase = True

    def timer_start(self):
        self.timer += 1

    def effect_dur(self, player):
        if self.timer >= 540:
            player.phase = False
            return True
        return False
    
    def update(self, player):
        if self.collected:
            self.timer_start() 
            self.effect_dur(player)

class barricade():
    def __init__(self):
        self.name = "barricade"
        self.rect = pygame.Rect(random.randint(0,1255), random.randint(0,695), 25, 25)
        self.can_place = False
        
    def draw(self, screen):
        pygame.draw.rect(screen, (173, 240, 255), self.rect)

    def collision(self, player ,Obstacles):
        if pygame.Rect.colliderect(self.rect, player.rect):
            self.rect.x = 2000
            self.can_place = True
        keys = pygame.key.get_pressed()

        if self.can_place and keys[pygame.K_RSHIFT]:
            Obstacles.append(obstacles.wall())    
            Obstacles[-1].rect.x = player.rect.x 
            Obstacles[-1].rect.y = player.rect.bottom
            self.can_place = False
    