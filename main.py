from player import Perso
from random import *
import pygame

pygame.init()

loop = True

clock = pygame.time.Clock()

ecranX = 800
ecranY = 450

fond = pygame.image.load('fond.png')

pygame.mixer.music.load("musique.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

myfont = pygame.font.SysFont("Ariel", 16)

ecran = pygame.display.set_mode((ecranX, ecranY))
pygame.display.set_caption("TRON - Alexis D'Ambrosio")

p = Perso()
p.x = randint(ecranX/10, ecranX-(ecranX/10))
p.y = randint(ecranY/10, ecranY-(ecranY/10))
p.color = "blue"

p2 = Perso()
p2.x = randint(ecranX/10, ecranX-(ecranX/10))
p2.y = randint(ecranY/10, ecranY-(ecranY/10))
p2.color = "orange"

rectX = randint(ecranX/10, ecranX-(ecranX/10))
rectY = randint(ecranY/10, ecranY-(ecranY/10))

while loop:

    clock.tick(60)

    ecran.blit(fond,(0,0))



    title = myfont.render("TRON", 0, (125,253,254))
    ecran.blit(title, (ecranX-(ecranX/1.9), 10))

    score_display1 = myfont.render("Joueur 1: " + str(p.score), 0, (125,253,254))
    ecran.blit(score_display1, (10, 10))

    score_display2 = myfont.render("Joueur 2: " + str(p2.score), 0, (125,253,254))
    ecran.blit(score_display2, (ecranX-125, 10))

    rect = pygame.draw.circle(ecran, (255, 255, 255), (rectX, rectY), 10)

    if p.x >= rectX-15 and p.x <= rectX+15:
        if p.y >= rectY-15 and p.y <= rectY+15:
            rectX = randint(ecranX/10, ecranX-(ecranX/10))
            rectY = randint(ecranY/10, ecranY-(ecranY/10))
            p.score = p.score + 1
            p2.vit = p2.vit*1.1

    if p2.x >= rectX-15 and p2.x <= rectX+15:
        if p2.y >= rectY-15 and p2.y <= rectY+15:
            rectX = randint(ecranX/10, ecranX-(ecranX/10))
            rectY = randint(ecranY/10, ecranY-(ecranY/10))
            p2.score = p2.score + 1
            p.vit = p.vit*1.1

    if p.x > ecranX:
        loop = False
    elif p.x < 0:
        loop = False
    elif p.y > ecranY:
        loop = False
    elif p.y < 0:
        loop = False

    if p2.x > ecranX:
        loop = False
    elif p2.x < 0:
        loop = False
    elif p2.y > ecranY:
        loop = False
    elif p2.y < 0:
        loop = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                p.dir = "up"
            if event.key == pygame.K_q:
                p.dir = "left"
            if event.key == pygame.K_s:
                p.dir = "down"
            if event.key == pygame.K_d:
                p.dir = "right"
            if event.key == pygame.K_p:
                loop = False

            if event.key == pygame.K_UP:
                p2.dir = "up"
            if event.key == pygame.K_LEFT:
                p2.dir = "left"
            if event.key == pygame.K_DOWN:
                p2.dir = "down"
            if event.key == pygame.K_RIGHT:
                p2.dir = "right"
            if event.key == pygame.K_p:
                loop = False

        if event.type == pygame.QUIT:
            loop = False
    p.Update(ecran)
    p.Draw(ecran)


    p2.Update(ecran)
    p2.Draw(ecran)

    pygame.display.flip()
pygame.quit()
