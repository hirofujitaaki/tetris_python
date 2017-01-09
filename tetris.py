import sys
import pygame
from blocks import Blocks
from settings import Settings


def main():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    settings = Settings(screen)
    blocks = Blocks(screen)
    pygame.display.set_caption("Tetris")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw walls.
        settings.draw_walls(blocks)
        # draw bottom.
        settings.draw_bottom(blocks)

        pygame.display.update()

        # drop a square.
        t = 0
        while t < 20:
            y = t + 1
            blocks.squares(5, y, settings.red)
            pygame.display.update()
            blocks.squares(5, y, settings.black)
            t = t + 1


if __name__ == '__main__':
    main()
