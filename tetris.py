import sys
import pygame


def run_game():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("Tetris")
    black = (0, 0, 0)
    white = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)

        # wall on the left.
        wall_times = 0
        while wall_times < 20:
            y_times = 0
            y_position = 0 + wall_times * 14
            while y_times < 12:
                x_times = 0
                x_position = 0
                while x_times < 12:
                    pygame.draw.rect(screen, white, (x_position, y_position, 1, 1,))
                    pygame.display.update()
                    x_position = x_position + 1
                    x_times = x_times + 1
                y_position = y_position + 1
                y_times = y_times + 1

            y_times = 0
            y_position = 0 + wall_times * 14
            while y_times < 12:
                x_times = 0
                x_position = 154
                while x_times < 12:
                    pygame.draw.rect(screen, white, (x_position, y_position, 1, 1))
                    pygame.display.update()
                    x_position = x_position + 1
                    x_times = x_times + 1
                y_position = y_position + 1
                y_times = y_times + 1
            wall_times = wall_times + 1

        # wall on the bottom.
        bottom_times = 0
        while bottom_times < 10:
            x_times = 0
            x_position = 14 + bottom_times * 14
            while x_times < 12:
                y_times = 0
                y_position = 266
                while y_times < 12:
                    pygame.draw.rect(screen, white, (x_position, y_position, 1, 1))
                    pygame.display.update()
                    y_position = y_position + 1
                    y_times = y_times + 1
                x_position = x_position + 1
                x_times = x_times + 1
            bottom_times = bottom_times + 1

        # update a portion of screen.

run_game()
