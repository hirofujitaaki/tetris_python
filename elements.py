import pygame


def squares(x_block_number, y_block_number, screen, color, horizontal_blocks=0, vertical_blocks=0):
    y_times = 0
    # Increace every 14 pixels in the y-axis.
    y_block_num = y_block_number * 14 + vertical_blocks * 14
    # Increace every 14 pixels in the x-axis.
    x_block_num = x_block_number * 14 + horizontal_blocks * 14
    while y_times < 12:
        x_times = 0
        x_blk_num = x_block_num
        while x_times < 12:
            pygame.draw.rect(screen, color, (x_blk_num, y_block_num, 1, 1))
            x_blk_num = x_blk_num + 1
            x_times = x_times + 1
        y_block_num = y_block_num + 1
        y_times = y_times + 1
