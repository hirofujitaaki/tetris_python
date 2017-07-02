import pygame


class Block():

    def __init__(self, screen):
        self.screen = screen
        self.macro = {}  # to check the collisions

    def square(self, x, y, color):
        """used to paint back to black also. so fill_macro() can't be included."""
        x_starting_pixel = x * 14
        y_starting_pixel = y * 14
        # a single square is by 12 * 12 pixels. mirgin is 2 pixels
        pygame.draw.rect(self.screen, color, (x_starting_pixel, y_starting_pixel, 12, 12))

    def fill_macro(self, x, y):
        """set the macro True."""
        self.macro[(x, y)] = True

    def draw_walls(self, color):
        ver_block_num = 0
        while ver_block_num < 20:
            self.square(0, ver_block_num, color)  # left
            self.square(11, ver_block_num, color)  # right

            self.fill_macro(0, ver_block_num)
            self.fill_macro(11, ver_block_num)

            ver_block_num = ver_block_num + 1

    def draw_bottom(self, color):
        hori_block_num = 1
        while hori_block_num < 11:
            self.square(hori_block_num, 19, color)
            self.fill_macro(hori_block_num, 19)

            hori_block_num = hori_block_num + 1
