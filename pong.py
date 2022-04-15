import random
from select import kevent
from string import whitespace
from time import sleep
import pygame
pygame.init()
fps = pygame.time.Clock()
pygame.key.set_repeat(1, 25)
score = [0, 0]
xwindow = 700
ywindow = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
dis=pygame.display.set_mode((xwindow,ywindow))
paddle1pos = 300
paddle2pos = 300
ballpos = [350, 350]
game_over = False
velocity = [1, random.randrange(-10, 10)/10]
def draweverything():
    paddle1 = pygame.draw.rect(dis, WHITE, pygame.Rect(600, paddle1pos, 10, 100))
    paddle2 = pygame.draw.rect(dis, WHITE, pygame.Rect(100, paddle2pos, 10, 100))
    ball = pygame.draw.rect(dis, WHITE, pygame.Rect(ballpos[0], ballpos[1], 10, 10))

def ballmove():
    global ballpos
    global velocity
    ballpos[0] = ballpos[0] + velocity[0] * 15
    ballpos[1] = ballpos[1] + velocity[1] * -15
    if ballpos[0] == 590 and ballpos[1] <= paddle1pos + 107 and ballpos[1] >= paddle1pos-7:
        velocity[0] = -1
        landed = paddle1pos + 100 - ballpos[1]
        velocity[1] = (50 - landed) * -.02
    if ballpos[0] == 110 and ballpos[1] <= paddle2pos + 107 and ballpos[1] >= paddle2pos-7:
        velocity[0] = 1
        landed = paddle2pos + 100 - ballpos[1]
        velocity[1] = (50 - landed) * -.02
    if ballpos[1] >= 700 or ballpos[1] <= 0:
        velocity[1] = velocity[1] * -1 
    if ballpos[0] >= 700:
        score[0] += 1
        sleep(1)
        velocity = [1, random.randrange(-10, 10)/10]
        ballpos = [350, 350]
    if ballpos[0] <= -10:
        score[1] += 1
        sleep(1)
        velocity = [-1, random.randrange(-10, 10)/10]
        ballpos = [350, 350]
def makescore():
    my_font = pygame.font.SysFont('freesansbold', 50)
    if score[0] == 5 or score[1] == 5:
        gameover_surface = my_font.render("Player " + str(score.index(5) + 1) + " Wins!", True, (BLUE))
        gameover_rect = gameover_surface.get_rect()
        gameover_rect.center = (350, 350)
        dis.blit(gameover_surface, gameover_rect)
        sleep(1)
        game_over = True
    score_surface = my_font.render(str(score[0]) + " - " + str(score[1]), True, (255, 255, 255))
    score_rect = score_surface.get_rect()
    score_rect.center = (350, 50)
    dis.blit(score_surface, score_rect)
def paddlemove():
    global paddle1pos, paddle2pos
    if paddle1pos <= 0:
        paddle1pos = 0
    if paddle2pos <= 0:
        paddle2pos = 0
    if paddle1pos >= 600:
        paddle1pos = 600
    if paddle2pos >= 600:
        paddle2pos = 600
while not game_over:
    dis.fill(BLACK)
    makescore()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle1pos -= 7
            paddlemove()
        if keys[pygame.K_DOWN]:
            paddle1pos += 7
            paddlemove()
        if keys[pygame.K_w]:
            paddle2pos -= 7
            paddlemove()
        if keys[pygame.K_s]:
            paddle2pos += 7
            paddlemove()
    ballmove()
    draweverything()
    pygame.display.update()
    fps.tick(20)

pygame.quit()
quit()