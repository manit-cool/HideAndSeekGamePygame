import player, pygame, random, powerups, powerup_managing_system, powerup_management_seeker, obstacles, time
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
        self.powerup_management_seeker = powerup_management_seeker.powerup_manager(self.screen, self.Seeker)
        self.collidables = []

        self.collidables.append(self.Hider)
        self.collidables.append(self.Seeker)
        self.collidables.append(self.powerup_management.powerup[0])
        self.collidables.append(self.powerup_management.powerup[1])  
        self.collidables.append(self.powerup_management.powerup[2])
        self.collidables.append(self.powerup_management_seeker.powerup[0])
        self.collidables.append(self.powerup_management_seeker.powerup[1])  
        self.collidables.append(self.powerup_management_seeker.powerup[2])
        self.obstacles = []
        
        for i in range(random.randint(10, 15)):
            self.obstacles.append(obstacles.wall())

        self.obstacles[-1].rect.center = self.Seeker.rect.center
        self.obstacles[-1].rect.top = self.Seeker.rect.bottom
    
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
            self.powerup_management_seeker.update_powerups(self.obstacles)

            pygame.display.flip()

            if self.Seeker.rect.colliderect(self.Hider.rect):         
                my_font = pygame.font.SysFont('Arial', 30)
                
                text = my_font.render("Game Over.", True, (255,25,2))
                
                pygame.draw.rect(self.screen, (2,2,2), (0, 0, 2000, 2000))
                
                self.screen.blit(text, (140, 150))

                pygame.display.flip()

                time.sleep(5)
                self.__init__()

            self.clock.tick(120) 


main = Main()
main.update()