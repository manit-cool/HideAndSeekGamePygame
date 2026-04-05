import player, pygame, random, powerups, powerup_managing_system, obstacles
# a cool nice and fun game :D
# really cool and fun hide and seek game :D

class Main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
    
        #player defines 
        self.Hider  = player.player(pygame.Vector2(100, 100), 1.5, 1)
        self.Seeker = player.player(pygame.Vector2(254, 100), 1.75,0)
        
        #powerups
        self.powerup_management = powerup_managing_system.powerup_manager(self.screen, self.Hider, self.Seeker) # this one is for the player!
        self.powerup_management_seeker = None
        self.collidables = []
        self.collidables.append(self.Hider)
        self.collidables.append(self.Seeker)
        self.collidables.append(self.powerup_management.powerup[0])
        self.collidables.append(self.powerup_management.powerup[1])  
 
        self.obstacles = []
        for i in range(random.randint(10, 15)):
            self.obstacles.append(obstacles.wall())

    def update(self):
        while self.running:
 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("white")
            for i in self.obstacles:
                i.update(self.screen, self.collidables)
 
            #Drawing
            self.Hider.draw((80, 157, 230), self.screen)
            self.Seeker.draw((50, 201, 83), self.screen)

            self.Hider.movement()
            self.Seeker.movement_arrow_pad()
            self.powerup_management.update_powerups()
            pygame.display.flip()   
            self.clock.tick(120) 

main = Main()

main.update()