class Settings():
    """A class to store all settings for Tetris."""

    def __init__(self,  screen):
        self.screen = screen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

    def draw_walls(self, block):
        vertical_blocks = 0
        while vertical_blocks < 20:
            block.square(0, vertical_blocks, self.white)  # left
            block.square(11, vertical_blocks, self.white)  # right

            block.fill_macro(0, vertical_blocks)  # set macro True.
            block.fill_macro(11, vertical_blocks)  # same as above.

            vertical_blocks = vertical_blocks + 1

    def draw_bottom(self, block):
        horizontal_blocks = 1
        while horizontal_blocks < 11:
            block.square(horizontal_blocks, 19, self.white)

            block.fill_macro(horizontal_blocks, 19)  # set macro True.

            horizontal_blocks = horizontal_blocks + 1
