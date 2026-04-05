import pygame

# vector2, speed

class player():
    def __init__(self, player_pos, speed, name):
        #Vectors,
        self.player_pos = player_pos
        self.dir = pygame.Vector2(0, 0)
        #Factor changing movement,
        self.speed = speed
        #player rect
        self.rect = pygame.Rect(self.player_pos.x, self.player_pos.y, 25, 25)
        #player defines,
        # hider = 1
        # seeker= 0
        self.name = name

        # this is for a powerup :3
        self.phase  = False

    def draw(self, color, surface):
        pygame.draw.rect(surface, color, self.rect)

    def movement(self):
        keys = pygame.key.get_pressed()
        self.rect.x = self.player_pos.x
        self.rect.y = self.player_pos.y
        self.dir.x = 0
        self.dir.y = 0

        if keys[pygame.K_a]:
            self.dir.x = -1
        if keys[pygame.K_d]:
            self.dir.x =  1
        if keys[pygame.K_s]:
            self.dir.y = 1
        if keys[pygame.K_w]:
            self.dir.y = -1
        
        # we need to do this line to make sure the vector dir's length is always 1!
        if pygame.math.Vector2.length(self.dir) > 0:
            self.dir = pygame.math.Vector2.normalize(self.dir)

        self.player_pos.x += self.dir.x * self.speed
        self.player_pos.y += self.dir.y * self.speed

    def movement_arrow_pad(self):
        keys = pygame.key.get_pressed()
        self.rect.x = self.player_pos.x
        self.rect.y = self.player_pos.y
        self.dir.x = 0
        self.dir.y = 0

        if keys[pygame.K_LEFT]:
            self.dir.x = -1
        if keys[pygame.K_RIGHT]:
            self.dir.x =  1
        if keys[pygame.K_DOWN]:
            self.dir.y = 1
        if keys[pygame.K_UP]:
            self.dir.y = -1
        
        # we need to do this line to make sure the vector dir's length is always 1!
        if pygame.math.Vector2.length(self.dir) > 0:
            self.dir = pygame.math.Vector2.normalize(self.dir)

        self.player_pos.x += self.dir.x * self.speed
        self.player_pos.y += self.dir.y * self.speed

