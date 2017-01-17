import pygame


class Block():

    def __init__(self, screen, macro):
        self.screen = screen
        self.macro = macro

    def square(self, x, y, color):  # red, white, or black.
        x_starting_pixel = x * 14
        y_starting_pixel = y * 14
        pygame.draw.rect(self.screen, color, (x_starting_pixel, y_starting_pixel, 12, 12))

    def fill_macro(self, x, y):
        self.macro[(x, y)] = True

    def check_macro(self, x, y):
        try:
            return self.macro[(x, y)]
        except KeyError:
            return False

    def slide_n_update(self, y, color_w, color_b):
        """ slide down all squares and update the macro. """
        y = y - 1
        while y >= 0:
            x = 1
            while x <= 10:
                if self.check_macro(x, y):
                    self.square(x, y, color_b)
                    self._clear_macro(x, y)
                    self.square(x, y+1, color_w)
                    self.fill_macro(x, y+1)
                x += 1
            y -= 1

    def remove_n_clear(self, y, color):
        """ remove squares in a raw and set the macro False. """
        x = 1
        while x < 11:
            self.square(x, y, color)  # black only
            self._clear_macro(x, y)
            x += 1

    def is_removeable(self, y):
        x = 1
        removeable = True
        while x < 11:
            removeable = removeable and self.check_macro(x, y)
            x += 1
        return removeable

    def _clear_macro(self, x, y):
        self.macro[(x, y)] = False

    def figure_sub_squares(self, x, y, r, typ):
        if typ == 0:
            if (r + 4) % 4 == 0:
                self.x1 = x + 1
                self.y1 = y
                self.x2 = x - 1
                self.y2 = y
            elif (r + 4) % 4 == 1:
                self.x1 = x
                self.y1 = y + 1
                self.x2 = x
                self.y2 = y - 1
            elif (r + 4) % 4 == 2:
                self.x1 = x - 1
                self.y1 = y
                self.x2 = x + 1
                self.y2 = y
            elif (r + 4) % 4 == 3:
                self.x1 = x
                self.y1 = y - 1
                self.x2 = x
                self.y2 = y + 1
        if typ == 1:
            if (r + 4) % 4 == 0:
                self.x1 = x + 1
                self.y1 = y
                self.x2 = x
                self.y2 = y - 1
            elif (r + 4) % 4 == 1:
                self.x1 = x
                self.y1 = y + 1
                self.x2 = x + 1
                self.y2 = y
            elif (r + 4) % 4 == 2:
                self.x1 = x - 1
                self.y1 = y
                self.x2 = x
                self.y2 = y + 1
            elif (r + 4) % 4 == 3:
                self.x1 = x
                self.y1 = y - 1
                self.x2 = x - 1
                self.y2 = y
