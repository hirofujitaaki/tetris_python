import sys
import pygame
from block import Block
from settings import Settings


def main():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("Tetris")

    macro = {}  # to check collisions.
    block = Block(screen, macro)
    settings = Settings(screen)
    settings.draw_walls(block)
    settings.draw_bottom(block)

    x = 5
    y = 1
    t = 0
    while True:

        # x1 = x
        # y1 = y
        # if r == 0:
        #     x1 = x + 1
        # elif r == 1:
        #     y1 = y + 1
        # elif r == 2:
        #     x1 = x - 1
        # elif r == 3:
        #     y1 = y - 1

        # draw the active block in red.
        block.square(x, y, settings.red)
        block.square(x+1, y, settings.red)

        pygame.display.update()

        # paint it back to black.
        block.square(x, y, settings.black)
        block.square(x+1, y, settings.black)

        x_move = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_move = 1

                elif event.key == pygame.K_LEFT:
                    x_move = -1

                # elif event.key == pygame.K_UP:
                #     r = r + 1
                #     if r == 4:
                #         r = 0

        x += x_move
        if block.check_macro(x, y) or block.check_macro(x+1, y) is True:
            x = x - x_move

        t += 1
        if t % 10 == 0:  # adjust the speed of falling blocks.
            y += 1

            if block.check_macro(x, y) or block.check_macro(x+1, y) is True:
                y = y - 1
                block.square(x, y, settings.white)
                block.square(x+1, y, settings.white)
                block.fill_macro(x, y)
                block.fill_macro(x+1, y)
                if block.is_removeable(y):
                    block.remove_n_clear(y, settings.black)
                    block.slide_n_update(y, settings.white, settings.black)
                x = 5
                y = 1


if __name__ == '__main__':
    main()
