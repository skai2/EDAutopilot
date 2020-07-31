def bright(image=None, testing=False):
    while True:
        if testing:
            img = get_screen((5/16)*SCREEN_WIDTH, (5/8)*SCREEN_HEIGHT,(2/4)*SCREEN_WIDTH, (15/16)*SCREEN_HEIGHT)
        else:
            img = image.copy()
        equalized = equalize(img)
        equalized = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
        equalized = cv2.cvtColor(equalized, cv2.COLOR_BGR2HSV)
        filtered = cv2.inRange(equalized, array([0, 0, 215]), array([0, 0, 255]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered