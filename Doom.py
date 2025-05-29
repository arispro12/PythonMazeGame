import pygame
import time
from pygame.key import get_pressed

pygame.init() #xekinaei to ergostaseio pygame
pygame.display.set_caption('Maze Of Doom') # dq maze of doom!!!!!!!!!!!!!!!!!!!!!!!!111111111
icon = pygame.image.load('Maze Of Doom.png')
pygame.mixer.init()
ts1 = time.time()
ts2 = time.time()
tol2 =0
tol3 = 0

pygame.mixer_music.load("Maze Of Doom.mp3")
pygame.mixer_music.play(-1)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1000,800))# fteiaxnei parathiro screen me diastaseis 400,300
Font = pygame.font.SysFont("comicsansms",50,True,True)
Font2 = pygame.font.SysFont("comicsansms",30,True,True)
tfont = pygame.font.SysFont("comicsansms",30,True,True)
tfont2 = pygame.font.SysFont("comicsansms",30,True,True)
done = False #metabliti false
sb = 0
sr = 0
xb = 30
yb = 30
xr = 925
yr = 30
def text(): #the text defining
    global tol2 , tfont , tfont2 , tol3
    Title = Font.render("Maze Of Doom", True, (0, 255, 0))
    screen.blit(Title, (300, 0))
    title2 = Font2.render("Made by arispro", True, (0, 255, 0))
    screen.blit(title2, (300, 70))
    tb = tfont.render(str(tol2),True,(0,0,255))
    screen.blit(tb,(30,30))
    tr = tfont2.render(str(tol3), True, (255, 0, 0))
    screen.blit(tr, (925, 30))
clock = pygame.time.Clock()
while done==False: #oso to done einai false to paixnidi paizei
    for event in pygame.event.get():  #energopoisou molis o paixths kanei event
        if event.type == pygame.QUIT: #an o paixths patisi esc,x
            done = True #stamataei to while
    screen.fill((0,0,0))
    text()
    player1 = pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(xb, yb, 60, 60)) #emfanizei
    player2 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xr, yr, 60, 60))# emfanizei
    player3 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(500, 370, 60, 60))
    w1 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(100, 0, 60, 600))
    w2 = pygame.draw.rect(screen,(184, 84, 57),pygame.Rect(850,0,60,600))
    w3 = pygame.draw.rect(screen,(184, 84, 57),pygame.Rect(400,300,60,60))
    w4 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(400, 450, 60, 60))
    w5 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(600, 450, 60, 60))
    w6 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(600, 300, 60, 60))
    w7 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(250, 200, 60, 600))
    w8 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(700, 200, 60, 600))
    wtrapblue = pygame.draw.rect(screen, (0,128,255), pygame.Rect(310, 200, 200, 60))
    wtrapred = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500, 200, 200, 60))
    if player1.bottom >screen.get_rect().bottom:
        yb -= 3
    if player1.top <screen.get_rect().top:
        yb += 3
    if player1.left >screen.get_rect().left:
        xb -= 3
    if player1.right <screen.get_rect().right:
        xb += 3
    if player2.bottom >screen.get_rect().bottom:
        yr -= 3
    if player2.top <screen.get_rect().top:
        yr += 3
    if player2.left >screen.get_rect().left:
        xr -= 3
    if player2.right <screen.get_rect().right:
        xr += 3


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: yr =yr -1
    if pressed[pygame.K_DOWN]: yr = yr +1
    if pressed[pygame.K_RIGHT]: xr = xr + 1
    if pressed[pygame.K_LEFT]: xr = xr - 1
    if pressed[pygame.K_w]: yb =yb -1
    if pressed[pygame.K_s]: yb = yb +1
    if pressed[pygame.K_d]: xb = xb + 1
    if pressed[pygame.K_a]: xb = xb - 1
    if player1.colliderect(player2):
        xb = 30
        yb = 30
        xr = 925
        yr = 30
    if player1.colliderect(player3):
            xb = 30
            te1 = time.time()
            tol2 = round(te1 - ts1, 2)
            print(tol2)
            ts1 = time.time()
            yb = 30
    if player2.colliderect(player3):
        te2 = time.time()
        tol3 = round(te2 - ts2, 2)
        print(tol2)
        ts2 = time.time()
        print(tol3)

        xr = 925
        yr = 30
    if player1.colliderect(w1) or player1.colliderect(w2) or player1.colliderect(w3) or player1.colliderect(w4) or player1.colliderect(w5) or player1.colliderect(w6) or player1.colliderect(w7) or player1.colliderect(w8) :
        if pressed[pygame.K_w]: yb += 10
        if pressed[pygame.K_s]: yb -= 10
        if pressed[pygame.K_a]: xb += 10
        if pressed[pygame.K_d]: xb -= 10
    if player2.colliderect(w1) or player2.colliderect(w2) or player2.colliderect(w3) or player2.colliderect(w4) or player2.colliderect(w5) or player2.colliderect(w6) or player2.colliderect(w7) or player2.colliderect(w8):
        if pressed[pygame.K_UP]: yr += 10
        if pressed[pygame.K_DOWN]: yr -= 10
        if pressed[pygame.K_LEFT]: xr += 10
        if pressed[pygame.K_RIGHT]: xr -= 10
    if player2.colliderect(wtrapblue):
        yr = 30
        xr = 925
    if player1.colliderect(wtrapred):
        yb = 30
        xb = 30
    pygame.display.flip() #teleutea entolh panta kai eaitias ths blepoume to parathiro
    clock.tick(100000000000000)