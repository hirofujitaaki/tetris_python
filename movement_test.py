import sys
import pygame
import elements


def main():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("Tetris")
    white = (255, 255, 255)
    black = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        t = 0
        while t < 20:
            y = t + 1
            elements.squares(1, y, screen, white)
            elements.squares(1, y, screen, black)
            pygame.display.update()
            t = t + 1


if __name__ == '__main__':
    main()
