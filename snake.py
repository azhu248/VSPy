import pygame
import random
pygame.init()
xwindow = 300
ywindow = 300
dis=pygame.display.set_mode((xwindow,ywindow))
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
SNAKE_HEAD = pygame.Color(255, 0, 255)
BLACK = pygame.Color(0, 0, 0)
fps = pygame.time.Clock()
snakeposx = [250, 240, 230, 220]
snakeposy = [250, 250, 250, 250]
xv = 0
yv = 0
fruit_xpos = 1
fruit_ypos = 1
fruit_xpos = random.randrange(0, xwindow/10) * 10
fruit_ypos = random.randrange(0, ywindow/10) * 10
def make_snake(): 
    for x in range(len(snakeposx)):
        if x == 0:
            snake = pygame.draw.rect(dis, SNAKE_HEAD, pygame.Rect(snakeposx[x], snakeposy[x], 10, 10))
        else:
            snake = pygame.draw.rect(dis, RED, pygame.Rect(snakeposx[x], snakeposy[x], 10, 10))
def move_snake():
    for x in reversed(range(len(snakeposx))):
        if dir == "right" or dir == "up" or dir == "left" or dir == "down":
            if x > 0:   
                snakeposx[x] = snakeposx[x-1]
                snakeposy[x] = snakeposy[x-1]
    if dir == "right":
        snakeposx[0] += 10
    if dir == "up":
        snakeposy[0] += -10
    if dir == "left":
        snakeposx[0] += -10
    if dir == "down":
        snakeposy[0] += 10
        

game_over=False
while not game_over:
    dis.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != "down":
                dir = "up"
            if event.key == pygame.K_DOWN and dir != "up":
                dir = "down"
            if event.key == pygame.K_RIGHT and dir != "left":
                dir = "right"
            if event.key == pygame.K_LEFT and dir != "right":
                dir = "left"
    move_snake()
    make_snake()
    if snakeposx[0] > xwindow or snakeposx[0] < 0 or snakeposy[0] > ywindow or snakeposy[0] < 0:
        game_over = True
    if snakeposx[0] == fruit_xpos and snakeposy[0] == fruit_ypos: #fruit collision
        snakeposx.append(snakeposx[-1]-10)
        snakeposy.append(snakeposy[-1]-10)
        fruit_xpos = random.randrange(0, xwindow/10) * 10
        fruit_ypos = random.randrange(0, xwindow/10) * 10
    for x in range(1,len(snakeposx)):
        if snakeposx[0] == snakeposx[x] and snakeposy[0] == snakeposy[x]:
            game_over = True
    fruit = pygame.draw.rect(dis, GREEN, pygame.Rect(fruit_xpos, fruit_ypos, 10, 10))
    pygame.display.update()






pygame.quit()
quit()