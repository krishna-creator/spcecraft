import pygame
import random
import math
from pygame import mixer
#sound=AudioSegment.from_mp3("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/background.mp3")
#sound.export("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/l.wa",format="wav")
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
screen=pygame.display.set_mode((800,600))#display screen
icon=pygame.image.load("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/dist/spacecraft/spaceship.png")
pygame.display.set_icon(icon)#sets the icon
pygame.display.set_caption("spacecraft")#sets the cation
background = pygame.image.load("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/dist/spacecraft/back.jpg")
background= pygame.transform.scale(background,(800,600))
mixer.music.load("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/dist/spacecraft/background.mp3")
mixer.music.play(-1)#adds the music throughtout the game
#score card
score_level=0
font=pygame.font.Font('freesansbold.ttf',32)
scoreX=10
scoreY=10
#adding spaceship image
playerimg=pygame.image.load("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/dist/spacecraft/player.png")
playerX=370
playerY=480
playerX_change=0
#adding alien
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemies=6
for i in range(no_of_enemies):
    enemyimg.append(pygame.image.load("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/dist/spacecraft/alien.png"))
    enemyX.append(random.randint(0,734))
    enemyY.append(random.randint(25,125))
    enemyX_change.append(3)
    enemyY_change.append(40)
#adding bullet
bulletimg=pygame.image.load("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/dist/spacecraft/bullet.png")
bullet_state="ready"
bulletY=480
bulletX=0
bulletY_change=10
#game over
gameover=pygame.font.Font('freesansbold.ttf',64)
game_state="run"
def game_over():
    global game_state
    game_state="end"
    g=gameover.render('GAME OVER',True,(255,255,255))
    screen.blit(g,(220,200))  
    mixer.quit()
def show_score(x,y):
    score=font.render('Score:'+str(score_level),True,(255,255,255))
    screen.blit(score,(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def bullet(x,y):
    global bullet_state
    bullet_state="fire" 
    screen.blit(bulletimg,(x+16,y+16))
def collision(x1,y1,x2,y2):
    distance=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    if distance<27:
        return True
    else:return False
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change-=5
            if event.key==pygame.K_RIGHT:
                playerX_change+=5
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/dist/spacecraft/bulletsound.wav")
                    bullet_sound.play()
                    bulletX=playerX
                    bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
    #player boundaries
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=734:
        playerX=734
    #enemy movement
    for i in range(no_of_enemies):
        if enemyY[i]>440:
            for j in range(no_of_enemies):
                enemyY[j]=1000
            game_over()
            show_score(330,260)            
            break
        #enemy boundaries
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]+=3
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=734:
            enemyX_change[i]-=3
            enemyY[i]+=enemyY_change[i] 
        #for collison
        collide=collision(bulletX,bulletY,enemyX[i],enemyY[i])
        if collide and bullet_state=="fire":
            bulletY=480
            bullet_state="ready"
            score_level+=100
            explosion_sound=mixer.Sound("C:/Users/vamsi/OneDrive/Desktop/projects/python projects/explosion_x.wav")
            explosion_sound.play()
            enemyX[i]=random.randint(0,734)
            enemyY[i]=random.randint(25,125)    
        enemy(enemyX[i],enemyY[i],i)
    #bullet movement
    if bulletY<=0:
        bullet_state="ready"
        bulletY=480
    if bullet_state is "fire":
        bulletY-=bulletY_change
        bullet(bulletX,bulletY)   
    if game_state is "run":
        player(playerX,playerY)
        show_score(scoreX,scoreY)
    pygame.display.update()
    

