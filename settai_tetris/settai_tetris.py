import pygame
import random
from block import Block
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf


def main():
    # initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((266, 838))
    pygame.display.set_caption('settai tetris')

    # instantiate the objects
    block = Block(screen)
    settings = Settings(screen)
    stats = GameStats(settings)
    sb = Scoreboard(screen, settings, stats)
    block.draw_outer(settings.white, settings.black)

    # create the Sound objects
    move_sound = pygame.mixer.Sound("sounds/move.wav")
    rotate_sound = pygame.mixer.Sound("sounds/rotate.wav")
    aeon_open = pygame.mixer.Sound("sounds/aeon_opening.wav")
    aeon_close = pygame.mixer.Sound("sounds/aeon_closing.wav")
    bottom_down = pygame.mixer.Sound("sounds/bottom_down.wav")

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
        # if collisions, put the pos back to previous one
        if block.check_macros(x_pos, y_pos):
            if block.x_move != 0:
                x_pos -= block.x_move
            elif block.r_move != 0:
                rotate -= block.r_move
        # otherwise ping a sound
        else:
            if block.x_move != 0:
                move_sound.play()
            elif block.r_move != 0:
                rotate_sound.play()

        timing += 1  # adjust the speed of falling blocks.
        if timing % 10 == 0 or block.push_down:
            y_pos += 1

            block.figure_sub_squares(x_pos, y_pos, rotate, type_)
            if block.check_macros(x_pos, y_pos):
                y_pos = y_pos - 1
                block.figure_sub_squares(x_pos, y_pos, rotate, type_)
                block.draw_squares(x_pos, y_pos, settings.white)
                block.fill_macros(x_pos, y_pos)
                block.remove_n_slide(settings, stats, sb, aeon_open, aeon_close)

                # prepare for the next block
                x_pos = 5
                y_pos = 1
                rotate = 0
                type_ = random.randrange(0, 7)

        # adjusting the level
        if block.any_of_macro():
            block.level += 1
            if block.level == 2:
                bottom_down.play()
                block.bottom_down(settings)
            elif block.level <= 3:
                # polite way to gave over
                import pdb; pdb.set_trace()

        # draw the active block in red.
        block.figure_sub_squares(x_pos, y_pos, rotate, type_)
        block.draw_squares(x_pos, y_pos, settings.red)

        sb.show_score()
        pygame.display.update()

        # then paint it back to black.
        block.draw_squares(x_pos, y_pos, settings.black)


if __name__ == '__main__':
    main()
