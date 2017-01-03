import sys
import pygame
import elements


def main():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("Tetris")
    white = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw walls.
        block_numbers_y = 0
        while block_numbers_y < 20:
            elements.squares(0, 0, 0, block_numbers_y, screen, white)  # left
            elements.squares(154, 0, 0, block_numbers_y, screen, white)  # right

            block_numbers_y = block_numbers_y + 1

        # draw the bottom.
        block_numbers_x = 0
        while block_numbers_x < 10:
            elements.squares(14, 266, block_numbers_x, 0, screen, white)  # bottom

            block_numbers_x = block_numbers_x + 1


if __name__ == '__main__':
    main()
