def get_destination_offset(testing=False):
    destination_template = cv2.imread(resource_path("templates/destination.png"), cv2.IMREAD_GRAYSCALE)
    destination_width, destination_height = destination_template.shape[::-1]
    pt = (0, 0)
    width = (1/3)*SCREEN_WIDTH
    height = (1/3)*SCREEN_HEIGHT
    while True:
        screen = get_screen((1/3)*SCREEN_WIDTH, (1/3)*SCREEN_HEIGHT,(2/3)*SCREEN_WIDTH, (2/3)*SCREEN_HEIGHT)
        mask_orange = filter_orange2(screen)
#         equalized = equalize(screen)
        match = cv2.matchTemplate(mask_orange, destination_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.2
        loc = where( match >= threshold)
        for point in zip(*loc[::-1]):
                pt = point
        final_x = (pt[0] + ((1/2)*destination_width)) - ((1/2)*width)
        final_y = ((1/2)*height) - (pt[1] + ((1/2)*destination_height))
        if testing:
            cv2.rectangle(screen, pt, (pt[0] + destination_width, pt[1] + destination_height), (0,0,255), 2)
            cv2.imshow('Destination Found', screen)
            cv2.imshow('Destination Mask', mask_orange)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    if pt[0] == 0 and pt[1] == 0:
        result = None
    else:
        result = {'x':final_x, 'y':final_y}
    logging.debug('get_destination_offset='+str(result))
    return result