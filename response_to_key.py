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

    x = 10
    y = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elements.squares(x, y, screen, white)
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    elements.squares(x, y, screen, black)
                    x += 1

                if event.key == pygame.K_LEFT:
                    elements.squares(x, y, screen, black)
                    x += -1

                if event.key == pygame.K_DOWN:
                    elements.squares(x, y, screen, black)
                    y += 1


if __name__ == '__main__':
    main()
