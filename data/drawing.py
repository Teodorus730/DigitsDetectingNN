import pygame
from config import *
from indata import in_data

from musthave import *
from pprint import pprint

import warnings

# убрать runtime предупреждения
warnings.filterwarnings('ignore')

pygame.init()

width = 45
height = 45
margin = 5

size = (WIDTH * (margin + width) + margin, HEIGHT * (margin + height) + margin)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("neuron")

done = False

clock = pygame.time.Clock()

cells = [0 for _ in range(INP_DIM)]

lal = []
dem = [
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
]
n = 0
length = len(dem)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (width + margin)
            row = pos[1] // (width + margin)
            kek = row*WIDTH+col
            if kek < INP_DIM:
                cells[kek] = int(not cells[kek])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                lal += main(mem(cells))
            if event.key == pygame.K_SPACE:
                pprint(lal)
            if event.key == pygame.K_d:
                lal = []
            if event.key == pygame.K_t:
                print(in_data(cells))
            if event.key == pygame.K_LEFT:
                n = max(n-1, 0)
                cells = dem[n]
            if event.key == pygame.K_RIGHT:
                n = min(n+1, length-1)
                cells = dem[n]

    screen.fill("black")

    color = "white"

    for row in range(WIDTH):
        for col in range(HEIGHT):
            if cells[row*HEIGHT+col]:
                color = "cyan"
            pygame.draw.rect(screen, color, [col*width+margin*(col+1), row*height+margin*(row+1), width, height])
            color = "white"

    pygame.display.flip()
    clock.tick(60)
pprint(lal)
pygame.quit()
