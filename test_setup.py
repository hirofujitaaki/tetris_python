def slide(block, settings):
    y = 18
    while y > 10:
        x = 1
        while x < 11:
            if x != 5:
                block.square(x, y, settings.white)
                block.fill_macro(x, y)
            x += 1
        y -= 1
