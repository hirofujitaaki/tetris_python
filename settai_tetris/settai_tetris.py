import pygame
import random
from block import Block
from settings import Settings
import game_functions as gf


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
        block.x_move = 0
        block.r_move = 0

        gf.check_events(block)
        x_pos += block.x_move
        rotate += block.r_move

        block.figure_sub_squares(x_pos, y_pos, rotate, type_)
        if block.check_macros(x_pos, y_pos):
            if block.x_move != 0:
                x_pos -= block.x_move
            elif block.r_move != 0:
                rotate -= block.r_move

        timing += 1  # adjust the speed of falling blocks.
        if timing % 10 == 0 or block.push_down:
            y_pos += 1

            block.figure_sub_squares(x_pos, y_pos, rotate, type_)
            if block.check_macros(x_pos, y_pos):
                y_pos = y_pos - 1
                block.figure_sub_squares(x_pos, y_pos, rotate, type_)
                block.draw_squares(x_pos, y_pos, settings.white)
                block.fill_macros(x_pos, y_pos)
                block.remove_n_slide(settings.white, settings.black)

                x_pos = 5
                y_pos = 1
                rotate = 0
                type_ = random.randrange(0, 7)

        # draw the active block in red.
        block.figure_sub_squares(x_pos, y_pos, rotate, type_)
        block.draw_squares(x_pos, y_pos, settings.red)

        pygame.display.update()

        # then paint it back to black.
        block.draw_squares(x_pos, y_pos, settings.black)


if __name__ == '__main__':
    main()
