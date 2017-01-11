import pygame


class Block():

    def __init__(self, screen, macro):
        self.screen = screen
        self.macro = macro

    def squares(self, x_base_position, y_base_position, color, x_recurring=0, y_recurring=0):
        """draw a square for recurring times."""
        # Increase every 14 pixels in the y-axis.
        y_starting_posi = y_base_position * 14 + y_recurring * 14
        # Increase every 14 pixels in the x-axis.
        x_starting_posi = x_base_position * 14 + x_recurring * 14
        pygame.draw.rect(self.screen, color, (x_starting_posi, y_starting_posi, 12, 12))
        # self.fill_macro(x_starting_posi, y_starting_posi)

    def fill_macro(self, x, y):
        self.macro[(x, y)] = True

    def check_macro(self, x, y):
        try:
            return self.macro[(x, y)]
        except KeyError:
            return False
