class Settings():
    """A class to store all settings for Tetris."""

    def __init__(self,  screen):
        self.screen = screen
        self.white  = (255, 255, 255)
        self.black  = (0, 0, 0)
        self.red    = (255, 0, 0)
        self.point = 1  # Scoring
