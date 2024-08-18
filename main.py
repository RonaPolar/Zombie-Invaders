from ast import Return
from glob import glob
from platform import python_branch
import pygame
import random
import math
from pygame import mixer
#initialize

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()  
pygame.display.set_caption("Zombie Invaders")

#screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 600))
#music
mixer.music.load("soundfx/bgm.wav")
mixer.music.play(-1)
mixer.music.set_volume(.1)
bulletsound1 = mixer.Sound("soundfx/beam1.wav")
bulletsound2 = mixer.Sound("soundfx/beam2.wav")
bulletsound3 = mixer.Sound("soundfx/beam3.wav")
levelup = mixer.Sound("soundfx/levelup.wav")
damagesound = mixer.Sound("soundfx/level2.wav")
#background image

bg = pygame.image.load("images/background.jpg")
bg = pygame.transform.scale(bg, (500, 650)) 

poster = pygame.image.load("images/poster.png")
poster = pygame.transform.scale(poster, (500, 650)) 

game = "notgame"
#hide text
draw_text = "show"
hidetext_time = pygame.time.get_ticks() + 1000

#score

score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
textX = 0
textY = 0

#gameover 

gameover_font = pygame.font.Font("fonts/freedom.ttf", 55)
gameoverX = 80
gameoverY = 250
gameover_state = "inactive"
#leveuptext

#press space to play again
press_font = pygame.font.Font("fonts/freedom.ttf", 20)
pressX = 120
pressY = 300

#press space2 to play again
press2_font = pygame.font.Font("fonts/freedom.ttf", 20)
press2X = 120
press2Y = 440


levelup_font = pygame.font.Font("fonts/freedom.ttf", 32)
levelupX = 300
levelupY = 0

#damage boost text
damage_font = pygame.font.Font("fonts/freedom.ttf", 32)
damageX = 220
damageY = 0

#spaceship
spaceship = pygame.image.load("images/space1.png")
spaceship = pygame.transform.scale(spaceship, (75, 75)) 
spaceX = 220
spaceY = 500
spaceX_change = 0
space_status = "space1"

#lives
lives = 10
lives_font = pygame.font.Font('freesansbold.ttf', 20)
livesX = 0
livesY = 50
#spaceship 2

space2 = pygame.image.load("images/space2.png")
space2 = pygame.transform.scale(space2, (75, 75))
space2X = 220
space2Y = 500
space2X_change = 0

#spaceship 3

space3 = pygame.image.load("images/space3.png")
space3 = pygame.transform.scale(space3, (75, 75))
space3X = 220
space3Y = 500
space3X_change = 0

#bullet 1

bulletImg = pygame.image.load("images/bullet.png")
bulletImg.set_colorkey((0,0,0))
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_speed = 7
bullet_state = "ready"
bullet_damage = 10

#bullet 2

bullet2 = pygame.image.load("images/bullet2.png")
bullet2.set_colorkey((0,0,0))

#bullet 3

bullet3 = pygame.image.load("images/bullet3.png")
bullet3.set_colorkey((0,0,0))

#normal zombie
normzom = []
normzom_health = []
normzomX = []
normzomY = []
normzomY_change = []
normzomY_changeup = []
norm_enemies = 5

#medium zombie
mediumzom = []
mediumzom_health = []
mediumzomX = []
mediumzomY = []
mediumzomY_change = []
mediumzom_enemies = 7

#hard zombies
hardzom = []
hardzom_health = []
hardzomX = []
hardzomY = []
hardzomY_change = []
hardzom_enemies = 8




def zombiespawn():
    global normzom
    global normzom_health
    global normzomX
    global normzomY
    global normzomY_change

    for i in range(norm_enemies):
        normzom.append(pygame.image.load("images/normalzombie.png").convert_alpha())
        normzom_health.append(50)
        normzomX.append(random.randint(0, 429))
        normzomY.append(random.randint(0, 120))
        normzomY_change.append(0.15)

def mediumzomspawn():
    global mediumzom
    global mediumzom_health
    global mediumzomX
    global mediumzomY
    global mediumzomY_change

    for j in range(mediumzom_enemies):
        mediumzom.append(pygame.image.load("images/mediumzombie.png").convert_alpha())
        mediumzom_health.append(100)
        mediumzomX.append(random.randint(0, 429))
        mediumzomY.append(random.randint(0, 120))
        mediumzomY_change.append(0.17)

def hardzomspawn():
    global hardzom
    global hardzom_health
    global hardzomX
    global hardzomY
    global hardzomY_change

    for i in range(norm_enemies):
        hardzom.append(pygame.image.load("images/hardzombie.png").convert_alpha())
        hardzom_health.append(355)
        hardzomX.append(random.randint(0, 429))
        hardzomY.append(random.randint(0, 120))
        hardzomY_change.append(0.18)

#draw objects
def leveluptext(x, y):  
    levelup_print = levelup_font.render("Level up!", True, (255, 0, 0))
    screen.blit(levelup_print, (x, y))
def damagetext(x, y):  
    damage_print = damage_font.render("Damage Increases!", True, (0, 255, 0))
    screen.blit(damage_print, (x, y))   
def gameover(x, y):
    gameover_print = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover_print, (x, y))
def press(x, y):
    press_print = press_font.render("Press SPACE to retry", True, (255, 255, 255))
    screen.blit(press_print, (x, y))
def press2(x, y):
    press2_print = press2_font.render("Press SPACE to play", True, (255, 255, 255))
    screen.blit(press2_print, (x, y))
def scoreshow(x, y):
    score_print = score_font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_print, (x, y))
def space(x, y):
    screen.blit(spaceship, (x, y))

def spaceship2(x, y):
    screen.blit(space2, (x, y))

def spaceship3(x, y):
    screen.blit(space3, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 24, y + 10))

def fire_bullet2(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet2, (x + 1, y + 10))

def fire_bullet3(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet3, (x + 1, y + 10))

def normzombies(x, y, i):
    screen.blit(normzom[i], (x, y))

def mediumzombies(x, y, j):
    screen.blit(mediumzom[j], (x, y))

def hardzombies(x, y, k):
    screen.blit(hardzom[k], (x, y))


    

def isCollision(normzomX, normzomY, bulletX, bulletY):
    distance = math.sqrt(math.pow(normzomX - bulletX, 2) + (math.pow(normzomY - bulletY, 2)))
    if distance < 32 and space_status == "space1":
        return True
    elif distance < 37 and space_status == "space2":
        return True
    elif distance < 38 and space_status == "space3":
        return True
    else:
        return False
#Gameloop

def main():
    running = True
    while running:
        global bulletsound1
        global bulletsound2
        global bulletsound3
        global levelup
        global lives
        global bullet_state
        global space_status
        global spaceX
        global gameover_state
        global spaceX_change
        global bulletX
        global bulletY
        global space2X
        global space2X_change
        global space3X
        global space3X_change
        global score
        global bullet_damage
        global draw_text
        global hidetext_time
        global bulletY_speed
        global normzomY_change
        global mediumzomY_change
        global hardzomY_change
        global game
        
        clock.tick(120)
        #bg image
           
        
        screen.blit(bg, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if space_status == "space1":
                    if event.key == pygame.K_LEFT:
                        spaceX_change = -1.5
                    if event.key == pygame.K_RIGHT:
                        spaceX_change = 1.5
                if space_status == "space2":
                    if event.key == pygame.K_LEFT:
                        space2X_change = -1.7
                    if event.key == pygame.K_RIGHT:
                        space2X_change = 1.7
                if space_status == "space3":
                    if event.key == pygame.K_LEFT: 
                        space3X_change = -1.7
                        if score % 20 == 0:
                            space3X_change += -0.4
                    if event.key == pygame.K_RIGHT:
                        space3X_change = 1.7
                        if score % 20 == 0:
                            space3X_change += 0.4
                if event.key == pygame.K_SPACE:
                    game = "ingame"
                    gameover_state = "inactive"
                    score = 0
                    bullet_state = "fire"
                    space_status = "space1"
                    bullet_damage = 10
                    bulletY_speed = 7
                    for i in range(norm_enemies):
                        normzomX[i] = random.randint(0, 429)
                        normzomY[i] = random.randint(0, 120)
                        normzomY_change[i] = 0.15
                    
                    for i in range(mediumzom_enemies):
                        mediumzomX[i] = random.randint(0, 429)
                        mediumzomY[i] = random.randint(0, 120)
                        mediumzomY_change[i] = 0.17
                  
                    for i in range(hardzom_enemies):
                        hardzomX[i] = random.randint(0, 429)
                        hardzomY[i] = random.randint(0, 120)
                        hardzomY_change[i] = 0.18
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    spaceX_change = 0
                    space2X_change = 0
                    space3X_change = 0
        if bullet_state == "fire" and space_status == "space1":
            bulletX = spaceX
            fire_bullet(bulletX, bulletY)
        if bullet_state == "fire" and space_status == "space2":
            bulletX = space2X
            fire_bullet(bulletX, bulletY)
        if bullet_state == "fire" and space_status == "space3":
            bulletX = space3X
            fire_bullet(bulletX, bulletY)
                    
        
        #spaceship movement
        spaceX += spaceX_change
        if spaceX <= 0:
            spaceX = 0
        elif spaceX >= 425:
            spaceX = 425

        #spaceship 2 movement
        space2X += space2X_change
        if space2X <= 0:
            space2X = 0
        elif space2X>= 425:
            space2X = 425
        
        #spaceship 3 movement
        space3X += space3X_change
        if space3X <= 0:
            space3X = 0
        elif space3X>= 425:
            space3X = 425

        zombiespawn()
        mediumzomspawn()
        hardzomspawn()
        
        #zombie movements
        for i in range(norm_enemies):
            normzomY[i] += normzomY_change[i]
            
            collision = isCollision(normzomX[i], normzomY[i], bulletX, bulletY)
            if collision:
                bullet_state == "fire"
                bulletY = 500
                normzom_health[i] -= bullet_damage
                if normzom_health[i] == 0 or normzom_health[i] < 0:
                    score += 1
                    normzomX[i] = random.randint(0, 400)
                    normzomY[i] = random.randint(0, 0)
                    normzom_health[i] = 50 
                    if score >= 10:
                        bullet_damage = 20
                        
            if normzomY[i] > 500:
                for r in range(norm_enemies):
                    normzomX[r] = 1000
                    normzomY[r] = 1000
                gameover(gameoverX, gameoverY)
                press(pressX, pressY)
                gameover_state = "active"
                bullet_state = "ready"
                draw_text = "hide"
            normzombies(normzomX[i], normzomY[i], i)
                
        if score >= 10:
            
            space_status = "space2"
            for j in range(mediumzom_enemies):
                mediumzomY[j] += mediumzomY_change[j]
                
                collision = isCollision(mediumzomX[j], mediumzomY[j], bulletX, bulletY)
                if collision:
                    bulletY = 500
                    bullet_state == "fire"
                    mediumzom_health[j] -= bullet_damage
                    if mediumzom_health[j] == 0 or mediumzom_health[j] < 0:
                        score += 1
                        mediumzomX[j] = random.randint(0, 400)
                        mediumzomY[j] = random.randint(0, 0)
                        mediumzom_health[j] = 100
                        if score >= 20:
                            bullet_damage = 40
                if score % 10 == 0:
                    mediumzomY_change[j] += 0.0015
                
                if mediumzomY[j] > 500:
                    for r in range(mediumzom_enemies):
                        mediumzomX[r] = 1000
                        mediumzomY[r] = 1000
                    gameover(gameoverX, gameoverY)
                    press(pressX, pressY)
                    gameover_state = "active"
                    bullet_state = "ready"
                    draw_text = "hide"
            
                mediumzombies(mediumzomX[j], mediumzomY[j], j)

        if score >= 20:
            space_status = "space3"
            for k in range(hardzom_enemies):
                hardzomY[k] += hardzomY_change[k]
                
                collision = isCollision(hardzomX[k], hardzomY[k], bulletX, bulletY)
                if collision:
                    bulletY = 500
                    bullet_state == "fire"
                    hardzom_health[k] -= bullet_damage
                    if hardzom_health[k] == 0 or hardzom_health[k] < 0:
                        score += 1
                        hardzomX[k] = random.randint(0, 400)
                        hardzomY[k] = random.randint(0, 0)
                        hardzom_health[k] = 350
                if score % 20 == 0:
                    hardzomY_change[k] += 0.003
                    bullet_damage += 2.7
                    damagetext(damageX, damageY)
                    damagesound.play()
                if hardzomY[k] > 500:
                    for r in range(hardzom_enemies):
                        hardzomX[r] = 1000
                        hardzomY[r] = 1000
                    gameover(gameoverX, gameoverY)
                    press(pressX, pressY)
                    gameover_state = "active"
                    bullet_state = "ready"
                    draw_text = "hide"
                hardzombies(hardzomX[k], hardzomY[k], k)
                
        
        scoreshow(textX, textY)
        if draw_text == "show":
            leveluptext(levelupX, levelupY)
                
        # Bullet Movement
        if bulletY <= 0:
            bulletY = 500
            bullet_state == "fire"
            
        if bullet_state == "fire" and space_status == "space1":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_speed
            bulletsound1.play()
            bulletsound1.set_volume(.08)
        elif bullet_state == "fire" and space_status == "space2":                  
            fire_bullet2(bulletX, bulletY)
            bulletY -= bulletY_speed + 5
            bulletsound2.play()
            bulletsound2.set_volume(.08)
        elif bullet_state == "fire" and space_status == "space3":
            fire_bullet3(bulletX, bulletY)
            bulletY -= bulletY_speed + 10
            bulletsound3.play()
            bulletsound3.set_volume(.08)

        if space_status == "space1":
            space(spaceX, spaceY)
            draw_text = "hide"
        elif space_status == "space2":
            spaceship2(space2X, space2Y)
        elif space_status == "space3":
            spaceship3(space3X, space3Y)
            
        if game == "notgame":
            screen.blit(poster, (0, 0))
            press2(press2X, press2Y)
        
        if score == 10:
            draw_text = "show"
        if score > 16:
            draw_text = "hide"

        if score >= 20:
            draw_text = "show"         
        if score > 40:
            draw_text = "hide"

        if draw_text == "show":
            levelup.play()
        pygame.display.update()
main()

