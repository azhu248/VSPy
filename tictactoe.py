#TicTacToe
from time import sleep
import pygame

pygame.init()
turn = 1
xwindow = 300
ywindow = 300
dis=pygame.display.set_mode((xwindow,ywindow))
game_over = False
boardstate = ["null", "null", "null", "null", "null", "null", "null", "null", "null"]
playerX = pygame.image.load("X_ttt.png")
playerO = pygame.image.load("minesweeper.png")
def gameover():
    dis.fill((0, 0, 0))
    global turn
    my_font = pygame.font.SysFont('freesansbold', 50)
    if turn == 10:
        game_over_surface = my_font.render('Tie', True, (255, 255, 255))
    elif turn%2 == 0:
        print("O")
        game_over_surface = my_font.render('Player O Wins', True, (255, 255, 255))
    elif turn%2 == 1:
        print("X")
        game_over_surface = my_font.render('Player X Wins', True, (255, 255, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.center = (150, 150)
    dis.blit(game_over_surface, game_over_rect)
    pygame.display.update()

def printboard():
    board = [pygame.draw.rect(dis, (255, 255, 255), pygame.Rect(100, 0, 1, 300)), pygame.draw.rect(dis, (255, 255, 255), pygame.Rect(200, 0, 1, 300)), pygame.draw.rect(dis, (255, 255, 255), pygame.Rect(0, 100, 300, 1)), pygame.draw.rect(dis, (255, 255, 255), pygame.Rect(0, 200, 300, 1))]
def mouseclick():
    if pygame.mouse.get_pos()[0] <= 100:
        if pygame.mouse.get_pos()[1] <= 100:
            return (0, 0, 0)
        if pygame.mouse.get_pos()[1] <= 200 and pygame.mouse.get_pos()[1] >= 100:
            return (0, 100, 1)
        if pygame.mouse.get_pos()[1] <= 300 and pygame.mouse.get_pos()[1] >= 200:
            return (0, 200, 2)
    if pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[0] >= 100:
        if pygame.mouse.get_pos()[1] <= 100:
            return (100, 0, 3)
        if pygame.mouse.get_pos()[1] <= 200 and pygame.mouse.get_pos()[1]>= 100:
            return (100, 100, 4)
        if pygame.mouse.get_pos()[1] <= 300 and pygame.mouse.get_pos()[1] >= 200:
            return (100, 200, 5)
    if pygame.mouse.get_pos()[0] <= 300 and pygame.mouse.get_pos()[0] >= 200:
        if pygame.mouse.get_pos()[1] <= 100:
            return (200, 0, 6)
        if pygame.mouse.get_pos()[1] <= 200 and pygame.mouse.get_pos()[1]>= 100:
            return (200, 100, 7)
        if pygame.mouse.get_pos()[1] <= 300 and pygame.mouse.get_pos()[1] >= 200:
            return (200, 200, 8)
def makeimage(turn):
    if turn%2 == 0 and boardstate[mouseclick()[2]] == "null":
        dis.blit(playerX, (mouseclick()[0:2]))
        boardstate[mouseclick()[2]] = "X"
    if turn%2 == 1 and boardstate[mouseclick()[2]] == "null":
        dis.blit(playerO, (mouseclick()[0:2]))
        boardstate[mouseclick()[2]] = "O"
def wincon():
    global game_over
    for x in range(0, 3):
        if boardstate[x*3] == boardstate[x*3 + 1] == boardstate[x*3 + 2] and boardstate[x*3] != "null":
                game_over = True
        if boardstate[x] == boardstate[x + 3] == boardstate [x + 6] and boardstate[x] != "null":
                game_over = True
    if boardstate[0] == boardstate [4] == boardstate[8] and boardstate[0] != "null":
        game_over = True
    if boardstate[2] == boardstate[4] == boardstate[6] and boardstate[2] != "null":
        game_over = True
printboard()
while not game_over:
    print(boardstate)
    wincon()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            makeimage(turn)
            turn += 1
    if turn == 10:
        game_over = True
    pygame.display.update()
gameover()
sleep(1)
pygame.quit()
quit()