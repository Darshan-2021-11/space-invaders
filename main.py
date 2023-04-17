import pygame
import math
import random
from pygame import mixer
from player import Player
from laser import Laser
from enemy import Enemy1
from enemy import Enemy2

FRAMEWIDTH = 800
FRAMEHEIGHT = 600

# Intialize the pygame
pygame.init()

#functions
font = pygame.font.Font('freesansbold.ttf', 20)
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(surface, x, y):
    score = font.render("Score : " + str(scoreVal), True, (255, 255, 255))
    surface.blit(score, (x, y))
    
def show_level(surface, x, y):
    lvl_text = font.render("Level : " + str(level), True, (255, 255, 255))
    surface.blit(lvl_text, (x, y))
    
def game_over_text(surface):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    surface.blit(over_text, (200, 250))

# Create a screen w, h
screen = pygame.display.set_mode((FRAMEWIDTH, FRAMEHEIGHT))


# Background and scroll
background = pygame.image.load('images\\background.png').convert()
bgscroll = 0
# +1 is required for the for loop later on used i<bgtiles and not i<=bgtiles
bgtiles = math.ceil(FRAMEHEIGHT/ background.get_height()) + 1

# Clock
clock = pygame.time.Clock()

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images\\ufo.png').convert()
pygame.display.set_icon(icon)

# Level and score
level = 1
scoreVal = 0
# player
player = Player()

# laser
laser = Laser()
# enemy
enemies = [Enemy1(random.randint(0, 735), random.randint(50, 150), 3) for i in range(0, level*2 + 1)]
    
# Game loop
running = True

while running:
    screen.fill((0, 0, 0))

    
    # Background animation
    tmp1 = 0
    while(tmp1 < bgtiles):
        screen.blit(background, (0, -(background.get_height()*tmp1 + bgscroll)))
        tmp1 += 1
    bgscroll -= 3
    if abs(bgscroll) > abs(background.get_height()):
        bgscroll = 0

    # Show Player and its health
    player.showPlayer(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keystroke works
        if event.type == pygame.KEYDOWN:
            print(str(event.key) + " has been pressed.")
            if event.key == pygame.K_LEFT:
                player.dx = -3
            if event.key == pygame.K_RIGHT:
                player.dx = 3
            if event.key == pygame.K_SPACE:
                if laser.state == "ready":
                    laser.state = "fire"
                    laser.lx = player.x
                    laser.sound = mixer.Sound('music\\laser.wav')
                    laser.sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.dx = 0

    # Player controled movement
    player.x += player.dx

    if (player.x <= 0):
        player.x = 0
    elif (player.x >= 736):
        player.x = 736

    # Enemy movement
    tmp2 = Enemy1()
    if(len(enemies) > 0):
        for enemy in enemies:
            enemy.x += enemy.dx
            if enemy.x <= 0:
                enemy.dx = 3
                enemy.y += enemy.dy
            elif enemy.x >= 736:
                enemy.dx = -3
                enemy.y += enemy.dy

            if enemy.y >= player.y:
                game_over_text(screen)
                running = False

            if enemy.boolh:
                if random.random() < 0.02 and enemy.state !="fire":
                    enemy.state = "fire"
                    enemy.lx = enemy.x

            # Collision
            collision = enemy.isCollision(laser)
            if collision:
                collision_sound = mixer.Sound('music\\collision.wav')
                collision_sound.play()
                laser.state = "ready"
                laser.ly = player.y
                scoreVal += 1

                if enemy.boolh:
                    if enemy.reduceHealth(laser):
                        tmp2 = enemy
                else:
                    tmp2 = enemy

            enemy.renderImg(screen)
    else:
        level += 1
        enemies = [Enemy1(random.randint(0, 735), random.randint(50, 150), 3) for i in range(0, level*2 + 1)]
        for i in range(level):
            enemies[random.randint(0, len(enemies)-1)] = Enemy2(random.randint(0, 735), random.randint(50, 150), 3, random.randint(0, 1))
    # deleting enemies
    if(tmp2 in enemies):
        enemies.remove(tmp2)
        
    show_score(screen, 10, 10)
    show_level(screen, 700-10, 10)
    if(player.playerHealth <= 0):
        game_over_text(screen)
        running = False


    # laser movement
    laser.fire(screen, player)
    for enemy in enemies:
        if enemy.boolh:
            if enemy.fire(screen, player):
                player.currPlayerHealth -= enemy.damage

    if(player.playerHealth < 0):
        running = false
        game_over_text(screen)
    pygame.display.update()

    # Limit fps
    clock.tick(60)
