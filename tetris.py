import sys
import pygame
from block import Block
from settings import Settings


def main():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    settings = Settings(screen)
    block = Block(screen)
    pygame.display.set_caption("Tetris")

    x = 5
    y = 1
    while True:
        # draw walls.
        settings.draw_walls(block)
        # draw bottom.
        settings.draw_bottom(block)

        block.squares(x, y, settings.red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    block.squares(x, y, settings.black)
                    x += 1

                elif event.key == pygame.K_LEFT:
                    block.squares(x, y, settings.black)
                    x += -1

        block.squares(x, y, settings.black)
        y += 1

        # # drop a square.
        # t = 0
        # while t < 20:
        #     y = t + 1
        #     block.squares(5, y, settings.red)
        #     pygame.display.update()
        #     block.squares(5, y, settings.black)
        #     t = t + 1


if __name__ == '__main__':
    main()
