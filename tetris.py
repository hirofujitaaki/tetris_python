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
    r = 0
    typ = 0
    while True:
        x_move = 0
        r_move = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_move = 1

                elif event.key == pygame.K_LEFT:
                    x_move = -1

                elif event.key == pygame.K_UP:
                    r_move = 1

        x += x_move
        r += r_move
        block.figure_sub_squares(x, y, r, typ)
        if block.check_macro(x, y) or block.check_macro(block.x1, block.y1) or \
                block.check_macro(block.x2, block.y2) is True:
            if x_move != 0:
                x -= x_move
            elif r_move != 0:
                r -= r_move

        t += 1
        if t % 10 == 0:  # adjust the speed of falling blocks.
            y += 1
            block.figure_sub_squares(x, y, r, typ)
            if block.check_macro(x, y) or block.check_macro(block.x1, block.y1) or \
                    block.check_macro(block.x2, block.y2) is True:
                y = y - 1
                block.figure_sub_squares(x, y, r, typ)
                block.square(x, y, settings.white)
                block.square(block.x1, block.y1, settings.white)
                block.square(block.x2, block.y2, settings.white)
                block.fill_macro(x, y)
                block.fill_macro(block.x1, block.y1)
                block.fill_macro(block.x2, block.y2)
                while block.is_removeable(y):
                    block.remove_n_clear(y, settings.black)
                    block.slide_n_update(y, settings.white, settings.black)
                while block.is_removeable(block.y1):
                    block.remove_n_clear(block.y1, settings.black)
                    block.slide_n_update(block.y1, settings.white, settings.black)
                while block.is_removeable(block.y2):
                    block.remove_n_clear(block.y2, settings.black)
                    block.slide_n_update(block.y2, settings.white, settings.black)
                x = 5
                y = 1
                r = 0
                typ = 1 - typ

        # draw the active block in red.
        block.square(x, y, settings.red)
        block.figure_sub_squares(x, y, r, typ)
        block.square(block.x1, block.y1, settings.red)
        block.square(block.x2, block.y2, settings.red)

        pygame.display.update()

        # paint it back to black.
        block.square(x, y, settings.black)
        block.square(block.x1, block.y1, settings.black)
        block.square(block.x2, block.y2, settings.black)


if __name__ == '__main__':
    main()
