import pygame
import random
import math
from pygame import mixer
pygame.init() #this is compulsory so as to initialise all the modules in pygame

screen = pygame.display.set_mode((800,600))

running = True
#background
#background=pygame.image.load("back.jpg")
mixer.music.load("7th_sense_chinese.mp3")
mixer.music.play(-1)

#title and icon
pygame.display.set_caption("virus invader")
icon = pygame.image.load("virus.png")
pygame.display.set_icon(icon)

#player logo
playerImg = pygame.image.load("pharmacist.png")
playerX=370
playerY=480
playerX_change=0

#enemy logo
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies =8


for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50,200))
    enemyX_change.append(0.6)
    enemyY_change.append(60)

#bullet
bulletImg = pygame.image.load("animals.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=2
bullet_state = "ready"

#player function in order to display
def player(x,y) :
    screen.blit(playerImg,(x,y))

#enemy function
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

#bullet function
def bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+10,y+10))

#collision detection
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2))
    if distance < 32:
        return True
    else:
        return False
    
#score    
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10
def show_score(x,y):
    score = font.render("SCORE : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))




#game loop 
while running:
    screen.fill((0,0,0))
   # screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change=0.8
            if event.key == pygame.K_LEFT:
                playerX_change= -0.8
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound=mixer.Sound("gun.wav")
                    bullet_sound.play()
                    bulletX=playerX
                    bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                playerX_change = 0
        
   
    playerX+=playerX_change
    
    #boundries to the player
    if playerX <= 0:
        playerX=0
    if playerX >= 736 :
        playerX=736
    
    #boundaries to enemy
    for i in range (no_of_enemies):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.8
            enemyY[i]+=enemyY_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -0.8
            enemyY[i]+=enemyY_change[i]
       #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            kill_sound=mixer.Sound("kill.wav")
            kill_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value += 1
            #print(score)
            enemyX[i]=random.randint(0, 735)
            enemyY[i]=random.randint(50,200)
        enemy(enemyX[i],enemyY[i],i)
        if  isCollision(enemyX[i],enemyY[i],playerX,playerY):
            running = False
            
    
    
    #bullet movement
    if bulletY <= 0:
        bulletY=480
        bullet_state="ready"
    if bullet_state == "fire":
        bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    player(playerX,playerY)
   
     
    show_score(textX, textY)
    pygame.display.update()

pygame.quit()
        
    

