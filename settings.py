class Settings():
    """A class to store all settings for Tetris."""

    def __init__(self,  screen):
        # Screen settings.
        self.screen = screen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

    def draw_walls(self, block):
        vertical_blocks = 0
        while vertical_blocks < 20:
            block.squares(0, 0, self.white, y_recurring=vertical_blocks)  # left
            block.squares(11, 0, self.white, y_recurring=vertical_blocks)  # right

            # set the macro True.
            block.fill_macro(0, vertical_blocks)
            block.fill_macro(11, vertical_blocks)

            vertical_blocks = vertical_blocks + 1

    def draw_bottom(self, block):
        horizontal_blocks = 0
        while horizontal_blocks < 10:
            block.squares(1, 19, self.white, x_recurring=horizontal_blocks)

            # set the macro True.
            block.fill_macro(horizontal_blocks+1, 19)

            horizontal_blocks = horizontal_blocks + 1
