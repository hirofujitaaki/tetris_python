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


def add_score(stats, settings, sb, aeon_open, aeon_close):
    stats.score += settings.point
    # bonus points. *5 points
    if (stats.score+1) % 3 == 0:
        aeon_open.play()
    if stats.score % 3 == 0:
        stats.score = stats.score * 5
        aeon_close.play()
    sb.prep_score()
