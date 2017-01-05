import sys
import pygame
import elements
from settings import Settings


def main():
    # Initialize the game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Tetris")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw walls.
        vertical_blocks = 0
        while vertical_blocks < 20:
            elements.squares(0, 0, screen, settings.white, vertical_blocks=vertical_blocks)  # left
            elements.squares(11, 0, screen, settings.white, vertical_blocks=vertical_blocks)  # right

            vertical_blocks = vertical_blocks + 1

        # draw bottom.
        horizontal_blocks = 0
        while horizontal_blocks < 10:
            elements.squares(1, 19, screen, settings.white, horizontal_blocks=horizontal_blocks)

            horizontal_blocks = horizontal_blocks + 1

        pygame.display.update()

        # drop a square.
        t = 0
        while t < 20:
            y = t + 1
            elements.squares(5, y, screen, settings.red)
            pygame.display.update()
            elements.squares(5, y, screen, settings.black)
            t = t + 1


if __name__ == '__main__':
    main()
