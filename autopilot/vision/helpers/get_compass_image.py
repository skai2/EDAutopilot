def get_compass_image(testing=False):
    compass_template = cv2.imread(resource_path("templates/compass.png"), cv2.IMREAD_GRAYSCALE)
    compass_width, compass_height = compass_template.shape[::-1]
    compass_image = compass_template.copy()
    doubt = 10
    while True:
        screen = get_screen((5/16)*SCREEN_WIDTH, (5/8)*SCREEN_HEIGHT,(2/4)*SCREEN_WIDTH, (15/16)*SCREEN_HEIGHT)
#         mask_orange = filter_orange(screen)
        equalized = equalize(screen)
        match = cv2.matchTemplate(equalized, compass_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.3
        loc = where( match >= threshold)
        pt = (doubt, doubt)
        for point in zip(*loc[::-1]):
                pt = point
        compass_image = screen[pt[1]-doubt : pt[1]+compass_height+doubt, pt[0]-doubt : pt[0]+compass_width+doubt].copy()
        if testing:
            cv2.rectangle(screen, pt, (pt[0] + compass_width, pt[1] + compass_height), (0,0,255), 2)
            cv2.imshow('Compass Found', screen)
            cv2.imshow('Compass Mask', equalized)
            cv2.imshow('Compass', compass_image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return compass_image, compass_width+(2*doubt), compass_height+(2*doubt)