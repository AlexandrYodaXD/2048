import pygame
import sys
from logic import *


def draw_interface():
    pretty_print(mas)

    pygame.draw.rect(screen, WHITE, title_rec)
    font = pygame.font.SysFont('stxingkai', 70)
    for row in range(blocks):
        for col in range(blocks):
            value = mas[row][col]
            text = font.render(f'{value}', True, BLACK)
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin + title_rec_h
            pygame.draw.rect(screen, COLORS[value], (x, y, size_block, size_block))
            if value != 0:
                font_x, font_y = text.get_size()
                text_x = x + (size_block - font_x) // 2
                text_y = y + (size_block - font_y) // 2
                screen.blit(text, (text_x, text_y))
    pygame.display.update()

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

COLORS = {
    0: (128, 128, 128),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 128, 255),
    32: (255, 0, 255),
    64: (128, 255, 255),
    128: (0, 255, 255),
}

ACTIONS = {
    'up': move_up,
    'left': move_left,
    'right': move_right,
    'down': move_down,
}

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

blocks = 4
size_block = 110
margin = 10
width = blocks * size_block + (blocks + 1) * margin
title_rec_w = width
title_rec_h = 110
height = width + title_rec_h
title_rec = pygame.Rect(0, 0, width, title_rec_h)

mas[1][2] = 2
mas[3][0] = 4

if __name__ == '__main__':
    print(get_empty_list(mas))
    pretty_print(mas)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('2048')
    draw_interface()

    while is_zero_in_mas(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.name(event.key)
                print(pressed_key)
                old_mas = [x.copy() for x in mas] # создает копию массива через генератор, потому что если делать чере .copy(), то внутренние списки не копируются, а на них создаются линки

                if pressed_key in ACTIONS:
                    mas = ACTIONS[pressed_key](mas)
                    # if event.key == pygame.K_LEFT:
                    #     # mas = move_left(mas)
                    #     mas = ACTIONS[pressed_key](mas)
                    # elif event.key == pygame.K_RIGHT:
                    #     mas = move_right(mas)
                    # elif event.key == pygame.K_UP:
                    #     mas = move_up(mas)
                    # elif event.key == pygame.K_DOWN:
                    #     mas = move_down(mas)
                if old_mas != mas:
                    mas = add_num(mas)
                    draw_interface()
        pygame.display.update()
