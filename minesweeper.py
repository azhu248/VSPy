import random
from time import sleep
import pygame
pygame.init()
dis=pygame.display.set_mode((900, 900))
boardimage = pygame.image.load("minesweeper.png")
onetile = pygame.image.load("1.png")
twotile = pygame.image.load("2.png")
threetile = pygame.image.load("3.png")
fourtile = pygame.image.load("4.png")
fivetile = pygame.image.load("5.png")
sixtile = pygame.image.load("6.png")
seventile = pygame.image.load("7.png")
eighttile = pygame.image.load("8.png")

dis.blit(boardimage, (0, 0))
turn = 0
game_over = False
box = []
bomb_surrounding = {}
for x in range(0, 9):
    for y in range(0, 9):
        box.append((x * 100,y * 100))
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
x = 1
while x <= 12:
    bomb_r = random.randrange(0, 9)
    bomb_c = random.randrange(0, 9)
    if board[bomb_r][bomb_c] == 1:
        continue
    else:
        board[bomb_r][bomb_c] = 1
        x += 1

def checkaround():
    # x1 = (x[0]+ 100, x[1] + 100)
    # x2 = (x[0]+ 100, x[1])
    # x3 = (x[0]+ 100, x[1] - 100)
    # x4 = (x[0], x[1] + 100)
    # x5 = (x[0], x[1] - 100)
    # x6 = (x[0]- 100, x[1] + 100)
    # x7 = (x[0]- 100, x[1])
    # x8 = (x[0]- 100, x[1] - 100)
    for x in range(0, 9):
        for y in range (0, 9):
            bombcount = 0
            try:
                if board[x + 1][y+ 1] == 1:
                    bombcount += 1
            except Exception:
                pass
            try:
                if board[x+ 1][y] == 1:
                    bombcount += 1
            except Exception:
                pass
            try:
                if board[x + 1][y - 1] == 1:
                    bombcount += 1
            except Exception:
                pass
            try:
                if board[x][y + 1] == 1:
                    bombcount += 1
            except Exception:
                pass
            try:
                if board[x][y - 1] == 1:
                    bombcount += 1
            except Exception:
                pass
            try:
                if board[x- 1][y + 1] == 1:
                    bombcount += 1
            except Exception:
                pass
            try:
                if board[x - 1][y] == 1:
                    bombcount += 1
            except Exception:
                pass
            try:
                if board[x - 1][y - 1] == 1:
                    bombcount += 1
            except Exception:
                pass
            bomb_surrounding.update({(x, y): bombcount})
    # if bombcount == 0:
    #     nobomblist.append(x)
    # print(nobomblist)
    # for item in nobomblist:
        
def click(clickpos):
    global game_over
    x = clickpos[0]//100
    y = clickpos[1]//100
    touching_zero_bomb_squares = []
    if board[x][y] == 0:
        if bomb_surrounding[(x, y)] == 0:
            touching_zero_bomb_squares = [(x, y)]
            print(touching_zero_bomb_squares)
            for item in touching_zero_bomb_squares:
                check = []
                check.append((item[0]+1, item[1]+1))
                check.append((item[0]+1, item[1]))
                check.append((item[0]+1, item[1]-1))
                check.append((item[0], item[1]+1))
                check.append((item[0], item[1]-1))
                check.append((item[0]-1, item[1]+1))
                check.append((item[0]-1, item[1]))
                check.append((item[0]-1, item[1]-1))
                for i in range(0, 8):
                    try:
                        if board[check[i][0]][check[i][1]] == 0:
                            if check[i][0] - item[0] <= 1 and check[i][0] - item[0] >= -1 and check[i][1] - item[1] >= -1 and check[i][1] - item[1] <= 1 and (check[i][0], check[i][1]) not in touching_zero_bomb_squares and bomb_surrounding[(check[i][0], check[i][1])] == 0:
                                touching_zero_bomb_squares.append((check[i][0], check[i][1]))
                    except Exception:
                        pass
                zerotiles = pygame.draw.rect(dis, (255, 0, 0), pygame.Rect(item[0] * 100, item[1] * 100, 100, 100))
                for iter in check:
                    try:
                        if bomb_surrounding[(iter[0]),(iter[1])] == 1: #ADD NUMS
                            dis.blit(onetile, (iter[0] * 100, iter[1] * 100))
                        if bomb_surrounding[(iter[0]),(iter[1])] == 2: #ADD NUMS
                            dis.blit(twotile, (iter[0] * 100, iter[1] * 100))
                        if bomb_surrounding[(iter[0]),(iter[1])] == 3: #ADD NUMS
                            dis.blit(threetile, (iter[0] * 100, iter[1] * 100))
                        if bomb_surrounding[(iter[0]),(iter[1])] == 4: #ADD NUMS
                            dis.blit(fourtile, (iter[0] * 100, iter[1] * 100))
                        if bomb_surrounding[(iter[0]),(iter[1])] == 5: #ADD NUMS
                            dis.blit(fivetile, (iter[0] * 100, iter[1] * 100))
                        if bomb_surrounding[(iter[0]),(iter[1])] == 6: #ADD NUMS
                            dis.blit(sixtile, (iter[0] * 100, iter[1] * 100))
                        if bomb_surrounding[(iter[0]),(iter[1])] == 7: #ADD NUMS
                            dis.blit(seventile, (iter[0] * 100, iter[1] * 100))
                        if bomb_surrounding[(iter[0]),(iter[1])] == 8: #ADD NUMS
                            dis.blit(eighttile, (iter[0] * 100, iter[1] * 100))
                    except Exception:
                        pass
        if bomb_surrounding[(x, y)] == 1: 
            dis.blit(onetile, (x * 100, y * 100))
        if bomb_surrounding[(x, y)] == 2: 
            dis.blit(twotile, (x * 100, y * 100))
        if bomb_surrounding[(x, y)] == 3: 
            dis.blit(threetile, (x * 100, y * 100))
        if bomb_surrounding[(x, y)] == 4: 
            dis.blit(fourtile, (x * 100, y * 100))
        if bomb_surrounding[(x, y)] == 5: 
            dis.blit(fivetile, (x * 100, y * 100))
        if bomb_surrounding[(x, y)] == 6: 
            dis.blit(sixtile, (x * 100, y * 100))
        if bomb_surrounding[(x, y)] == 7: 
            dis.blit(seventile, (x * 100, y * 100))
        if bomb_surrounding[(x, y)] == 8: 
            dis.blit(eighttile, (x * 100, y * 100))
    else:
        game_over = True        
while not game_over:
    checkaround()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = pygame.mouse.get_pos()[0]
            click_y = pygame.mouse.get_pos()[1]
            for x in box:
                if x[0] <= click_x and x[0] + 100 > click_x and x[1] <= click_y and x[1] + 100 > click_y:
                    print(x)
                    click(x)
for x in range(0, 9):
    for y in range (0, 9):
        if board[x][y] == 1:
            bomb = pygame.draw.rect(dis, (0, 255, 0), pygame.Rect(x * 100, y * 100, 100, 100))
pygame.display.update
pygame.quit()
quit()