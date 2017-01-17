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
            base = {'x1': -1, 'y1': 0, 'x2': 1, 'y2': 0, 'x3': 2, 'y3': 0}
            self._relative_positions(x, y, r, base)
        elif typ == 1:
            base = {'x1': -1, 'y1': -1, 'x2': -1, 'y2': 0, 'x3': 1, 'y3': 0}
            self._relative_positions(x, y, r, base)
        elif typ == 2:
            base = {'x1': -1, 'y1': 0, 'x2': 0, 'y2': -1, 'x3': 1, 'y3': 0}
            self._relative_positions(x, y, r, base)
        elif typ == 3:
            base = {'x1': -1, 'y1': 0, 'x2': 1, 'y2': -1, 'x3': 1, 'y3': 0}
            self._relative_positions(x, y, r, base)
        elif typ == 4:
            base = {'x1': -1, 'y1': 0, 'x2': 0, 'y2': 1, 'x3': 1, 'y3': 1}
            self._relative_positions(x, y, r, base)
        elif typ == 5:
            base = {'x1': 1, 'y1': 0, 'x2': 0, 'y2': 1, 'x3': 1, 'y3': 1}
            self._relative_positions(x, y, r, base)
        elif typ == 6:
            base = {'x1': 1, 'y1': 0, 'x2': -1, 'y2': 1, 'x3': 0, 'y3': 1}
            self._relative_positions(x, y, r, base)

    def _relative_positions(self, x, y, r, base):
        self.base = base
        while (r + 4) % 4 > 0:
            self.base['x1'], self.base['y1'] = self.base['y1'] * -1, self.base['x1']
            self.base['x2'], self.base['y2'] = self.base['y2'] * -1, self.base['x2']
            self.base['x3'], self.base['y3'] = self.base['y3'] * -1, self.base['x3']
            r -= 1
        self.base['x1'] += x
        self.base['y1'] += y
        self.base['x2'] += x
        self.base['y2'] += y
        self.base['x3'] += x
        self.base['y3'] += y
