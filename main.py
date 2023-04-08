import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()
font12 = pygame.font.Font("freesansbold.ttf", 15)
screen2 = pygame.Surface((screen_width, screen_height))
fps = 60

click = False
shake_amount = 5

clock = pygame.time.Clock()

circles = []


def shake(mag, dur, frames_ps):

    change = mag/dur
    mag -= change/frames_ps
    if random.randint(0, 1) == 0:
        x = mag
    else:
        x = -mag

    if random.randint(0, 1) == 0:
        y = mag
    else:
        y = -mag
    return x, y


path_radius = 100
width = 25
num = 5
# DO NOT GO OVER 100 WITH NUM
for i in range(num):
    circles.append([[random.randint(1, 5)], [screen_width/2, screen_height/2 - (path_radius * 2)], 0,
                    [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]])

for i in circles:
    r = random.randint(0, 500)
    for g in range(r):
        i[2] += 0.01
        i[1][0] += math.cos(i[2]) * 2
        i[1][1] += math.sin(i[2]) * 2

running = True
while running:
    mx, my = pygame.mouse.get_pos()

    screen2.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

    pygame.draw.circle(screen2, (200, 200, 200), (screen_width / 2, screen_height / 2), 200, 10)

    for i in circles:
        for w in circles:
            pygame.draw.line(screen2, (200, 200, 200), (i[1][0], i[1][1]), (w[1][0], w[1][1]), 1)

    for i in circles:
        for q in range(int(i[0][0])):
            i[2] += 0.01
            i[1][0] += math.cos(i[2]) * 2
            i[1][1] += math.sin(i[2]) * 2

    winning_score = 0
    for i in circles:
        for e in circles:
            if (e[2] - i[2]) > 0:
                i[0][0] += 0.0005 + (e[2] - i[2])/10000
                pygame.draw.circle(screen2, (0, 255, 0), (i[1][0], i[1][1]), width + 5, 5)
            if (e[2] - i[2]) < 0:
                i[0][0] -= 0.0005 + (e[2] - i[2])/10000
                pygame.draw.circle(screen2, (255, 0, 0), (i[1][0], i[1][1]), width + 5, 5)
            if i[2] >= winning_score:
                winning_score = i[2]
        pygame.draw.circle(screen2, i[3], (i[1][0], i[1][1]), width, 0)

    a = 0
    for i in circles:
        a += 20
        if i[2] == winning_score:
            screen2.blit(font12.render(str(i[2]), True, (0, 255, 0)), (screen_width - 100, 100 + a))
        else:
            screen2.blit(font12.render(str(i[2]), True, (255, 0, 0)), (screen_width - 100, 100 + a))

    if click:
        # x_shake, y_shake = shake(shake_amount, 10000, 60)
        screen.blit(screen2, (random.randint(-shake_amount, shake_amount), random.randint(-shake_amount, shake_amount)))
        # screen.blit(screen2, (x_shake, y_shake))
        # print(x_shake)
        # print(y_shake)
        # click = False
    else:
        screen.blit(screen2, (0, 0))

    pygame.display.update()
    clock.tick(fps)
