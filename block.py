import pygame


class Block():

    def __init__(self, screen):
        self.screen = screen

    # def squares(self, x_block_number, y_block_number, color, horizontal_blocks=0, vertical_blocks=0):
    #     """draw a certain number of squares. """
    #     y_times = 0
    #     # Increase every 14 pixels in the y-axis.
    #     y_block_num = y_block_number * 14 + vertical_blocks * 14
    #     # Increase every 14 pixels in the x-axis.
    #     x_block_num = x_block_number * 14 + horizontal_blocks * 14
    #     while y_times < 12:
    #         x_times = 0
    #         x_blk_num = x_block_num
    #         while x_times < 12:
    #             pygame.draw.rect(self.screen, color, (x_blk_num, y_block_num, 1, 1))
    #             x_blk_num = x_blk_num + 1
    #             x_times = x_times + 1
    #         y_block_num = y_block_num + 1
    #         y_times = y_times + 1

    def squares(self, x_base_position, y_base_position, color, x_recurring=0, y_recurring=0):
        """draw a square for recurring times."""
        # Increase every 14 pixels in the y-axis.
        y_starting_posi = y_base_position * 14 + y_recurring * 14
        # Increase every 14 pixels in the x-axis.
        x_starting_posi = x_base_position * 14 + x_recurring * 14
        pygame.draw.rect(self.screen, color, (x_starting_posi, y_starting_posi, 12, 12))
