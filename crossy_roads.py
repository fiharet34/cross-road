import pygame
import os
import random
pygame.init()
screen_x = 800
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
done = False
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
win = 0
my_image1 = pygame.image.load(os.path.join('тупо_вор.png'))
police1 = pygame.image.load(os.path.join('полиция_а.png'))
police2 = pygame.image.load(os.path.join( 'полиция_б.png'))
police_rects = []
def draw1():
    for i in range(1, 10):
        pygame.draw.rect(screen, GREY, (0, 700 - i * 70, screen_x, 70))
    for i in range(10):
        pygame.draw.rect(screen, WHITE, (0, 700 - i * 70, screen_x, 5))
class Gamer():
    def __init__(self):
        self.x = 350
        self.y = 702
        self.vy = 70
        self.vx = 70
        self.image = my_image1
        self.rect = self.image.get_rect(x=self.x, y=self.y)
    def move(self):
        self.y += self.vy
        self.rect.y += self.vy
        self.x += self.vx
        self.rect.x += self.vx           
    def draw2(self):       
        screen.blit(self.image, (self.x, self.y))
class Policia():
    def __init__(self, direc, y):
        self.x = random.randrange(-120, 920)
        self.y = y
        if direc == 0:
            self.v = 5
            self.image = police2
            self.original = -120
        else:
            self.image = police1
            self.v = -5
            self.original = 920
        self.rect = self.image.get_rect(x=self.x, y=self.y)
    def move(self):
        if self.x >= 921 or self.x <= -121:
            self.x = self.original
            self.rect.x = self.original
        self.x += self.v
        self.rect.x += self.v
    def draw(self):       
        screen.blit(self.image, (self.x, self.y))
chels = []
for n in range(1, 10):
    direct_policec = random.randrange(0, 2)
    for j in range(2):
        chels.append(Policia(direct_policec, n * 70 + 5))
        police_rects.append(chels[j].rect)
player = Gamer()
while not done:
    clock.tick(25)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.vy = -70
                player.vx = 0
                player.move()
            elif event.key == pygame.K_s:
                player.vy = 70
                player.vx = 0
                player.move()
            elif event.key == pygame.K_a:
                player.vy = 0
                player.vx = -70
                player.move()
            elif event.key == pygame.K_d:
                player.vy = 0
                player.vx = 70
                player.move()
    for i in range(len(chels)):
        if chels[i].rect.colliderect(player.rect):
            done = True
    draw1()
    player.draw2()
    for i in chels:
        i.move()
        i.draw()
    if player.y <= 2:
        done = True
    pygame.display.flip()

pygame.quit()