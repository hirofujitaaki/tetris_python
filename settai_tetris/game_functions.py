import sys
import pygame


def check_events(block):
    """Responds to keypresses."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                block.x_move = 1

            elif event.key == pygame.K_LEFT:
                block.x_move = -1

            elif event.key == pygame.K_UP:
                block.r_move = 1

            elif event.key == pygame.K_DOWN:
                block.push_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                block.push_down = False


def add_score(stats, settings, sb):
    stats.score += settings.point
    sb.prep_score()
