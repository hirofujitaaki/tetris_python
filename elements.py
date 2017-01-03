import pygame


def squares(x_position, y_position, color, screen, block_numbers_x=0, block_numbers_y=0):
    y_times = 0
    # Increace every 14 pixels in the y-axis.
    y_posi = y_position + block_numbers_y * 14
    # Increace every 14 pixels in the x-axis.
    x_positi = x_position + block_numbers_x * 14
    while y_times < 12:
        x_times = 0
        x_posi = x_positi
        while x_times < 12:
            pygame.draw.rect(screen, color, (x_posi, y_posi, 1, 1))
            pygame.display.update()
            x_posi = x_posi + 1
            x_times = x_times + 1
        y_posi = y_posi + 1
        y_times = y_times + 1
