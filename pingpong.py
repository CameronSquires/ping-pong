import pygame, sys
import random
import pygame.freetype



FPS=30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400,400), 0, 32)
WHITE = (255,255,255)
BLACK = (0,0,0)
SPEED = 7.5
VEL = 5.2
SCORELIMIT = 10
ANGLE = random.randint(-10,10)



class Top(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((0,0,400,1))
    def draw(self, surface):
        pygame.draw.rect(DISPLAYSURF, (BLACK), self.rect)

class Bottom(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((0,400,400,1))
    def draw(self, surface):
        pygame.draw.rect(DISPLAYSURF, (BLACK), self.rect)

class PlayerOneNet(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((0,0,1,400))
    def draw(self, surface):
        pygame.draw.rect(DISPLAYSURF, (BLACK), self.rect)

class PlayerTwoNet(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((400,0,1,400))
    def draw(self, surface):
        pygame.draw.rect(DISPLAYSURF, (BLACK), self.rect)

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((50,136,16,64))
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if self.rect.y>=0:
                self.rect.move_ip(0, -SPEED)
        if key[pygame.K_s]:
            if self.rect.y<=336:
                self.rect.move_ip(0, SPEED)
    def draw(self, surface):
        pygame.draw.rect(DISPLAYSURF, WHITE, self.rect)

class PlayerTwo(object):
    def __init__(self):
        self.rect = pygame.rect.Rect ((350, 136, 16, 64))
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if self.rect.y>=0:
                self.rect.move_ip(0, -SPEED)
        if key[pygame.K_DOWN]:
            if self.rect.y<=336:
                self.rect.move_ip(0, SPEED)
    def draw(self, surface):
        pygame.draw.rect(DISPLAYSURF, WHITE, self.rect)

class Ball(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((200, 190, 10, 10))

    def move(self):
        self.rect.move_ip(VEL, ANGLE)

    def draw(self, surface):
        pygame.draw.rect(DISPLAYSURF, WHITE, self.rect)

pygame.init()

def nextRound():
    global VEL
    global ANGLE
    global SCORELIMIT
    ball.rect.update(200, 190, 10, 10)
    player.rect.update(50,136,16,64)
    playertwo.rect.update(350, 136, 16, 64)
    i = random.randint(1,2)
    if i == 1:
        VEL = VEL

    if i == 2:
        VEL = -VEL
    ANGLE = random.randint(-10,10)
    pygame.display.update()

pts = 0
ptstwo = 0

pygame.display.set_caption(("PING! PONG!"))

player = Player()
playertwo = PlayerTwo()
ball = Ball()
top = Top()
bottom = Bottom()
playeronenet = PlayerOneNet()
playertwonet = PlayerTwoNet()

o = 1

i = random.randint(1,2)
if i == 1:
    VEL = VEL

if i == 2:
    VEL = -VEL


while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    top.draw(DISPLAYSURF)
    if ball.rect.colliderect(top):
        ANGLE = -ANGLE
    bottom.draw(DISPLAYSURF)
    if ball.rect.colliderect(bottom):
        ANGLE = -ANGLE
    player.move()
    player.draw(DISPLAYSURF)
    playertwo.move()
    playertwo.draw(DISPLAYSURF)
    ball.move()
    ball.draw(DISPLAYSURF)
    if ball.rect.colliderect(player):
        VEL = -VEL
        ANGLE = random.randint(-10,10)
        ball.rect.move_ip(10, 0)
    if ball.rect.colliderect(playertwo):
        VEL = -VEL
        ANGLE = random.randint(-10,10)
        ball.rect.move_ip(-10, 0)
    playeronenet.draw(DISPLAYSURF)
    playertwonet.draw(DISPLAYSURF)
    if ball.rect.colliderect(playertwonet):
        pts += 1
        nextRound()
    if ball.rect.colliderect(playeronenet):
        ptstwo += 1
        nextRound()
    if o == 1:
        pygame.display.update()
        pygame.time.wait(3000)
        o +=1
    font = pygame.font.Font("Hhenum-Regular.otf", 74)
    scoredisplay = font.render(str(pts), 1, WHITE)
    DISPLAYSURF.blit(scoredisplay, (100,10))
    scoredisplay = font.render(str(ptstwo), 1, WHITE)
    DISPLAYSURF.blit(scoredisplay, (300,10))

    if pts == SCORELIMIT:
        VEL = 0
        ANGLE = 0
        font = pygame.font.Font("Hhenum-Regular.otf", 22)
        windisplay = font.render("CONGRATS. PLAYER ONE WINS.", 1, WHITE)
        DISPLAYSURF.blit(windisplay, (85,75))
        

    if ptstwo == SCORELIMIT:
        VEL = 0
        ANGLE = 0
        font = pygame.font.Font("Hhenum-Regular.otf", 22)
        windisplay = font.render("CONGRATS. PLAYER TWO WINS.", 1, WHITE)
        DISPLAYSURF.blit(windisplay, (85,75))

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)