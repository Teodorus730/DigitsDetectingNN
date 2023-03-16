import pygame
from config import *
from prediction import predict

import warnings

# убрать runtime предупреждения
warnings.filterwarnings('ignore')

pygame.init()

width = 45
height = 45
margin = 5

cells_width = WIDTH * (margin + width) + margin
cells_height = HEIGHT * (margin + height) + margin
text_width = cells_width - 2 * margin
text_height = 50

size = (cells_width, cells_height + text_height + margin)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("neuron")

done = False

clock = pygame.time.Clock()

cells = [0 for _ in range(INP_DIM)]

text = pygame.font.SysFont('serif', 35).render("", False, "green")
text_rect = pygame.Rect(margin, cells_height, text_width, text_height)


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
            if event.key == pygame.K_SPACE:
                f, c, t = predict(cells, True)
                text = pygame.font.SysFont('serif', 35).render(t, False, c)

    screen.fill("black")

    color = "white"

    for row in range(WIDTH):
        for col in range(HEIGHT):
            if cells[row*HEIGHT+col]:
                color = "cyan"
            pygame.draw.rect(screen, color, [col*width+margin*(col+1), row*height+margin*(row+1), width, height])
            color = "white"

    pygame.draw.rect(screen, "#282828", text_rect)
    screen.blit(text, (text_rect.x, text_rect.y))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()