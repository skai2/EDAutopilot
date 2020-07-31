def get_sun_percent():
    screen = get_screen((1/3)*SCREEN_WIDTH, (1/3)*SCREEN_HEIGHT,(2/3)*SCREEN_WIDTH, (2/3)*SCREEN_HEIGHT)
    filtered = filter_sun(screen)
    total = (1/3)*SCREEN_WIDTH*(1/3)*SCREEN_HEIGHT
    white = sum(filtered == 255)
    black = sum(filtered != 255)
    result = white / black
    return result * 100