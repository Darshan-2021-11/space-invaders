import math
import pygame
class Enemy():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Enemy1(Enemy):
    def __init__(self, x=0, y=0, dx=0):
        super().__init__(x, y)
        self.dx = dx
        self.dy = 35
        self.boolh = False

        self.enemyImg = pygame.image.load('images/enemy1.png')

    def renderImg(self, surface):
        surface.blit(self.enemyImg, (self.x, self.y))

    def isCollision(self, laser):
        distance = math.sqrt(math.pow(self.x - laser.lx, 2) + math.pow(self.y - laser.ly, 2))
        if distance < 27:
            return True
        else:
            return False


    

class Enemy2(Enemy):
    laserImg = pygame.image.load('images/red laser.png')
    def __init__(self, x=0, y=0, dx=0, powerup=0):
        super().__init__(x, y)
        self.dx = dx
        self.dy = 35
        self.boolh = True
        self.health = 10
        self.powerup = powerup

        self.enemyImg = pygame.image.load('images/enemy2.png')

        self.lx = 0
        self.ly = 600
        self.ldy = 15
        self.state = "ready"
        self.damage = 4

    def renderImg(self, surface):
        surface.blit(self.enemyImg, (self.x, self.y))

    def isCollision(self, laser):
        distance = math.sqrt(math.pow(self.x - laser.lx, 2) + math.pow(self.y - laser.ly, 2))
        if distance < 27:
            return True
        else:
            return False

    def reduceHealth(self, laser):
        self.health -= laser.damage
        if(self.health < 0):
            return True
        else:
            return False

    def fire(self, surface, player):
        if self.ly > 600:
            self.ly = self.y
            self.state = "ready"

        # only for initialisation purpose, so the function returns false in main for reducing health of player
        distance = 100
        if self.state == "fire":
            surface.blit(Enemy2.laserImg, (self.lx + 16, self.ly + 10))
            self.ly += self.ldy
            distance = math.sqrt(math.pow(self.lx - player.x, 2) + math.pow(self.ly - player.y, 2))
            
        if distance < 27:
            return True
        else:
            return False
