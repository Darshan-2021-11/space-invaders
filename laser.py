import pygame

class Laser:
    laserImg = pygame.image.load('images\\laser.png')
    def __init__(self, dy=15):
        self.lx = 0
        self.ly = 600
        self.ldy = dy
        self.state = "ready"
        self.damage = 4

    
    def fire(self, surface, player):
        if self.ly < 0:
            self.ly = player.y
            self.state = "ready"
        
        if self.state == "fire":
            surface.blit(Laser.laserImg, (self.lx + 16, self.ly + 10))
            self.ly -= self.ldy

