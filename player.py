import pygame
class Perso:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.vit = 1
        self.dir = ""
        self.color = ""
        self.score = 0

    def Draw(self, ecran):
        pygame.draw.rect(ecran, (self.color), (self.x, self.y, 10, 10))

    def Collision(self, loop):
        if self.x > 500:
            loop = False
        elif self.x < 0:
            loop = False
        elif self.y > 500:
            loop = False
        elif self.y < 0:
            loop = False

    def Update(self, ecran):
        if self.dir == "up":
            self.y-=self.vit
        elif self.dir == "down":
            self.y+=self.vit
        elif self.dir == "left":
            self.x-=self.vit
        elif self.dir == "right":
            self.x+=self.vit
