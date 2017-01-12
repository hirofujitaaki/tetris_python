import sys
import pygame
from block import Block
from settings import Settings
import test_setup


def main():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("Tetris")

    macro = {}  # to check collisions.
    block = Block(screen, macro)
    settings = Settings(screen)
    x = 5
    y = 1
    t = 0
    test_setup.slide(block, settings)  # for testing purpose.
    while True:
        # draw walls.
        settings.draw_walls(block)
        # draw bottom.
        settings.draw_bottom(block)

        # draw the active block in red.
        block.square(x, y, settings.red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if block.check_macro(x+1, y) is False:
                        block.square(x, y, settings.black)
                        x += 1

                elif event.key == pygame.K_LEFT:
                    if block.check_macro(x-1, y) is False:
                        block.square(x, y, settings.black)
                        x += -1

        # paint it back to black.
        block.square(x, y, settings.black)

        # adjust the speed of falling blocks.
        t += 1
        if t % 10 == 0:
            # check collisions.
            if block.check_macro(x, y+1) is True:
                block.square(x, y, settings.white)
                block.fill_macro(x, y)
                if block.is_removeable(y):
                    block.remove_n_clear(y, settings.black)
                    block.slide_n_update(y, settings.white, settings.black)
                x = 5
                y = 1
            else:
                # keep falling down if no collisions.
                y += 1


if __name__ == '__main__':
    main()
