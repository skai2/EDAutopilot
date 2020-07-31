def get_screen(x_left, y_top, x_right, y_bot):
    """Gets screenshot specified by given coordinates"""
    screen = array(ImageGrab.grab(bbox=(x_left, y_top, x_right, y_bot)))
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen