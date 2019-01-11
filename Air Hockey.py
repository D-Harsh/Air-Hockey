import pygame, sys
from pygame import *
import time

FPS = 30
windowWidth = 1000
windowHeight = 500
lineThickness = 20
goalLength = 174
paddleSize = 100
paddleOffSet = 40

# Set up the colours
bgColor = (0, 0, 0)
fgColor = (255, 111, 111)


def drawArena(Color):
    display.fill((0, 0, 0))
    # pygame.draw.rect(display, fgColor, ((250, 150), (275, 175)))
    pygame.draw.rect(display, Color, ((0, 0), (windowWidth, windowHeight)), lineThickness * 2)
    pygame.draw.line(display, Color, (int((windowWidth / 2)), 0), (int((windowWidth / 2)), windowHeight),
                     int(lineThickness / 4))


def drawGoal(goal, goalColor):
    pygame.draw.rect(display, goalColor, goal)


def drawPaddle(paddle, paddle2, color):
    if paddle.y + 50 > windowHeight - lineThickness:
        paddle.y = windowHeight - lineThickness - 50
    if paddle.y - 50 < lineThickness:
        paddle.y = lineThickness + 50
    paddle2.y = paddle.y
    if paddle.x - 50 < lineThickness:
        paddle.x = lineThickness + 50
    if paddle.x + 50 > int(windowWidth / 2):
        paddle.x = windowWidth / 2 - 50
    paddle2.x = windowWidth - paddle.x
    pygame.draw.circle(display, color, (paddle.x, paddle.y), 50, 12)
    pygame.draw.circle(display, (100, 11, 33), (paddle.x, paddle.y), 38)
    pygame.draw.circle(display, color, (paddle2.x, paddle2.y), 50, 12)
    pygame.draw.circle(display, (100, 11, 33), (paddle2.x, paddle2.y), 38)


def displayScore(score,color):
    resultSurf = font.render('Score = %s' % (score), True, bgColor, color)
    resultRect = resultSurf.get_rect()
    resultRect.topright = (490, 25)
    display.blit(resultSurf, resultRect)


def displaytime(now,color):
    resultSurf = font.render('time = %s' % round(time.time() - now, 1), True, bgColor, color)
    resultRect = resultSurf.get_rect()
    resultRect.topright = (950, 25)
    display.blit(resultSurf, resultRect)


def main():
    pygame.init()
    global display
    global font
    FPSCLOCK = pygame.time.Clock()
    display = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Air Hockey")
    font = pygame.font.SysFont('freesansbold.ttf', 40)
    goal1 = pygame.Rect(lineThickness, (windowHeight / 2) - goalLength / 2, lineThickness, goalLength)
    goal2 = pygame.Rect(windowWidth - lineThickness * 2, (windowHeight / 2) - goalLength / 2, lineThickness, goalLength)
    paddle1 = pygame.draw.circle(display, fgColor, (windowWidth - lineThickness - 50, int(windowHeight / 2)), 50)
    paddle2 = pygame.draw.circle(display, fgColor, (windowWidth - lineThickness - 50, int(windowHeight / 2)), 50)
    paddle2.x = int(windowWidth - lineThickness - 50)
    paddle2.y = int(windowHeight / 2)
    score = 0
    color = 0
    colorState = True
    pygame.mouse.set_visible(0)
    now = time.time()

    while (score < 101):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                drawPaddle(paddle1, paddle2, bgColor)
                mousex, mousey = event.pos
                paddle1.y = mousey
                if mousex <= windowWidth:
                    paddle1.x = mousex
        if colorState:
            color += 2
        if color == 254:
            colorState = False
        elif color ==0:
            colorState = True
        if not colorState:
            color -= 2
        drawArena((color, 255 - color, color))
        drawGoal(goal1, (color, 255 - color, color))
        drawGoal(goal2, (color, 255 - color, color))
        drawPaddle(paddle1, paddle2, (color, 255 - color, color))
        displayScore(score, (color, 255 - color, color))
        displaytime(now, (color, 255 - color, color))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
