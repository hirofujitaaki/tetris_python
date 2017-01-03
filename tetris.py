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
        vertical_numbers = 0
        while vertical_numbers < 20:
            elements.squares(0, 0, white, screen, block_numbers_y=vertical_numbers)  # left
            elements.squares(154, 0, white, screen, block_numbers_y=vertical_numbers)  # right

            vertical_numbers = vertical_numbers + 1

        # draw bottom.
        horizontal_numbers = 0
        while horizontal_numbers < 10:
            elements.squares(14, 266, white, screen, block_numbers_x=horizontal_numbers)

            horizontal_numbers = horizontal_numbers + 1


if __name__ == '__main__':
    main()
