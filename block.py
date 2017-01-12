import pygame


class Block():

    def __init__(self, screen, macro):
        self.screen = screen
        self.macro = macro

    def square(self, x_position, y_position, color):
        x_starting_pixel = x_position * 14
        y_starting_pixel = y_position * 14
        pygame.draw.rect(self.screen, color, (x_starting_pixel, y_starting_pixel, 12, 12))

    def fill_macro(self, x, y):
        self.macro[(x, y)] = True

    def check_macro(self, x, y):
        try:
            return self.macro[(x, y)]
        except KeyError:
            return False

    def remove(self, y, color):
        if self._is_removeable(y):
            x = 1
            while x < 11:
                self.square(x, y, color)  # back to black.
                self._clear_macro(x, y)
                x += 1

    def _is_removeable(self, y):
        x = 1
        removeable = True
        while x < 11:
            removeable = removeable and self.check_macro(x, y)
            x += 1
        return removeable

    def _clear_macro(self, x, y):
        self.macro[(x, y)] = False
