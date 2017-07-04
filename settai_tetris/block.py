import pygame


class Block():

    def __init__(self, screen):
        self.screen = screen
        self.x_move = 0
        self.r_move = 0
        self.push_down = False  # drops the active block
        self.macro = {}  # to check the collisions

    def draw_square(self, x, y, color):
        """draw a 12*12 square. take 2 pixels for margin."""
        x_starting_pixel = x * 14
        y_starting_pixel = y * 14
        pygame.draw.rect(self.screen, color, (x_starting_pixel, y_starting_pixel, 12, 12))
        # used to paint back to black also, so fill_macro() can't be included.

    def draw_squares(self, x, y, color):
        self.draw_square(x, y, color)
        self.draw_square(self.base['x1'], self.base['y1'], color)
        self.draw_square(self.base['x2'], self.base['y2'], color)
        self.draw_square(self.base['x3'], self.base['y3'], color)

    def fill_macro(self, x, y):
        """set the macro True."""
        self.macro[(x, y)] = True

    def fill_macros(self, x, y):
        self.fill_macro(x, y)
        self.fill_macro(self.base['x1'], self.base['y1'])
        self.fill_macro(self.base['x2'], self.base['y2'])
        self.fill_macro(self.base['x3'], self.base['y3'])

    def draw_walls(self, color):
        ver_block_num = 0
        while ver_block_num < 20:
            self.draw_square(0, ver_block_num, color)  # left
            self.draw_square(11, ver_block_num, color)  # right

            self.fill_macro(0, ver_block_num)
            self.fill_macro(11, ver_block_num)

            ver_block_num = ver_block_num + 1

    def draw_bottom(self, color):
        hori_block_num = 1
        while hori_block_num < 11:
            self.draw_square(hori_block_num, 19, color)
            self.fill_macro(hori_block_num, 19)

            hori_block_num = hori_block_num + 1

    def check_macro(self, x, y):
        try:
            return self.macro[(x, y)]
        except KeyError:
            return False

    def check_macros(self, x, y):
        return self.check_macro(x, y) or \
               self.check_macro(self.base['x1'], self.base['y1']) or \
               self.check_macro(self.base['x2'], self.base['y2']) or \
               self.check_macro(self.base['x3'], self.base['y3'])

    def is_removable(self, y):
        """return True if a row is removable."""
        x = 1
        removable = True
        while x < 11:
            removable = removable and self.check_macro(x, y)
            x += 1
        return removable

    def _clear_macro(self, x, y):
        self.macro[(x, y)] = False

    def remove_n_clear(self, y, color):
        """ remove squares in a row and set the macro False. """
        x = 1
        while x < 11:
            self.draw_square(x, y, color)  # black only
            self._clear_macro(x, y)
            x += 1

    def slide_n_update(self, y, color_w, color_b):
        """ slide down all squares above and update the macro. """
        y = y - 1
        while y >= 0:
            x = 1
            while x <= 10:
                if self.check_macro(x, y):
                    self.draw_square(x, y, color_b)
                    self._clear_macro(x, y)
                    self.draw_square(x, y+1, color_w)
                    self.fill_macro(x, y+1)
                x += 1
            y -= 1

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
