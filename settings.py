class Settings():
    """A class to store all settings for Tetris."""

    def __init__(self,  screen):
        # Screen settings.
        self.screen = screen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

    def draw_walls(self, blocks):
        vertical_blocks = 0
        while vertical_blocks < 20:
            blocks.squares(0, 0, self.white, vertical_blocks=vertical_blocks)  # left
            blocks.squares(11, 0, self.white, vertical_blocks=vertical_blocks)  # right

            vertical_blocks = vertical_blocks + 1

    def draw_bottom(self, blocks):
        horizontal_blocks = 0
        while horizontal_blocks < 10:
            blocks.squares(1, 19, self.white, horizontal_blocks=horizontal_blocks)

            horizontal_blocks = horizontal_blocks + 1
