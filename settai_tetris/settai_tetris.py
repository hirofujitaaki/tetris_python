import sys
import pygame
from block import Block
from settings import Settings
import random


def main():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((266, 838))
    pygame.display.set_caption('settai tetris')

    block = Block(screen)
    settings = Settings(screen)
    block.draw_walls(settings.white)
    block.draw_bottom(settings.white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
