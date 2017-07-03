import sys
import pygame
from block import Block
from settings import Settings
import random


def main():
    # initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((266, 838))
    pygame.display.set_caption('settai tetris')

    # instantiate the objects
    block = Block(screen)
    settings = Settings(screen)
    block.draw_walls(settings.white)
    block.draw_bottom(settings.white)

    # set the initial blocl and the position
    x_pos = 5
    y_pos = 1
    timing = 0
    rotate = 0
    type_ = random.randrange(0, 7)

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

        x_pos += x_move
        rotate += r_move
        block.figure_sub_squares(x_pos, y_pos, rotate, type_)
        if block.check_macros(x_pos, y_pos):
            if x_move != 0:
                x_pos -= x_move
            elif r_move != 0:
                rotate -= r_move

        timing += 1
        if timing % 10 == 0:  # adjust the speed of falling blocks.
            y_pos += 1
            block.figure_sub_squares(x_pos, y_pos, rotate, type_)

            if block.check_macros(x_pos, y_pos):
                y_pos = y_pos - 1
                block.figure_sub_squares(x_pos, y_pos, rotate, type_)
                block.squares(x_pos, y_pos, settings.white)
                block.fill_macros(x_pos, y_pos)

                while block.is_removable(y_pos):
                    block.remove_n_clear(y_pos, settings.black)
                    block.slide_n_update(y_pos, settings.white, settings.black)
                while block.is_removable(block.base['y1']):
                    block.remove_n_clear(block.base['y1'], settings.black)
                    block.slide_n_update(block.base['y1'], settings.white, settings.black)
                while block.is_removable(block.base['y2']):
                    block.remove_n_clear(block.base['y2'], settings.black)
                    block.slide_n_update(block.base['y2'], settings.white, settings.black)
                while block.is_removable(block.base['y3']):
                    block.remove_n_clear(block.base['y3'], settings.black)
                    block.slide_n_update(block.base['y3'], settings.white, settings.black)
                x_pos = 5
                y_pos = 1
                rotate = 0
                type_ = random.randrange(0, 7)

        # draw the active block in red.
        block.figure_sub_squares(x_pos, y_pos, rotate, type_)
        block.squares(x_pos, y_pos, settings.red)

        pygame.display.update()

        # then paint it back to black.
        block.squares(x_pos, y_pos, settings.black)


if __name__ == '__main__':
    main()
