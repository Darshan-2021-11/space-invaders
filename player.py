import pygame

class Player():
    def __init__(self):
        self.playerImg = pygame.image.load('images/player.png')
        self.x = 370
        self.y = 520
        self.dx = 0
        self.playerHealth = 20
        self.currPlayerHealth = self.playerHealth
        self.healthFrac = self.currPlayerHealth/self.playerHealth

    def showPlayer(self, surface):
        self.healthFrac = self.currPlayerHealth/self.playerHealth
        health_font = pygame.font.Font('freesansbold.ttf',14)
        health_text = health_font.render("Player Health: ", True, (255, 255, 255))
        surface.blit(health_text, (10, 50))

        # default health
        pygame.draw.rect(surface, (255, 255, 255), (150, 50, 600, 20))
        # current health
        if(self.healthFrac < 0):
            return

        surface.blit(self.playerImg, (self.x, self.y))
        pygame.draw.rect(surface,((1-self.healthFrac)*255, self.healthFrac*255, 0), (152, 52, self.healthFrac*596, 16))
        
