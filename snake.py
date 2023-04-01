import pygame
import random
import sys

'''
fx, fy - координаты food задаются рандомно
dx, dy - diraction
'''
def gameover():
    run = False
    while run == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    gameLoop()
            elif event.type == pygame.QUIT:
                run = False
                sys.exit()
        pygame.display.update()
        clock.tick(15)
        win.blit(img2, (0, 0))
            
        
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('COBRA')
img = pygame.image.load('1.jpg').convert()
img2 = pygame.image.load('2.jpg').convert()

def gameLoop():
    x,y = 250, 250
    fx, fy = round(random.randrange(0, 480) / 10.0) * 10.0, round(random.randrange(0, 480) / 10.0) * 10.0
    size = 20
    length = 1
    speed = 5
    snake = []
    dx, dy = 0, 0
    d = 0
    run = True
    while run:
        pygame.time.delay(100)
              
        for event in pygame.event.get():          
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and d != 2:
                    dx, dy, d = -1, 0, 1
                if event.key == pygame.K_RIGHT and d != 1:
                    dx, dy, d = 1, 0, 2
                if event.key == pygame.K_UP and d != 4:
                    dx, dy, d = 0, -1, 3
                if event.key == pygame.K_DOWN and d != 3:
                    dx, dy, d = 0, 1, 4
                if event.key == pygame.K_q:
                    run = False
                    sys.exit()
        if not (0 < x < 500 and 0 < y < 500) or len(snake) != len(set(snake)):
            gameover()
                    
        win.blit(img, (0, 0))
        snake.append((x, y))
        snake = snake[-length:]
        [(pygame.draw.rect(win, (0,255,0), (i, j, size, size))) for i, j in snake]
        pygame.draw.rect(win, (255,0,0), (fx, fy, size, size))
        x += dx * size
        y += dy * size
        pygame.display.flip()
        clock.tick(speed)

        if (fx-10) <= x <= (fx+10) and (fy-10) <= y <= (fy+10):
            length += 1
            speed += 1
            fx = round(random.randrange(0, 480) / 10.0) * 10.0
            fy = round(random.randrange(0, 480) / 10.0) * 10.0

gameLoop()
pygame.quit()


