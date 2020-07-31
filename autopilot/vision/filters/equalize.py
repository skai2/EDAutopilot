def equalize(image=None, testing=False):
    """Equalizes received image"""
    while True:
        if testing:
            img = get_screen((5/16)*SCREEN_WIDTH, (5/8)*SCREEN_HEIGHT,(2/4)*SCREEN_WIDTH, (15/16)*SCREEN_HEIGHT)
        else:
            img = image.copy()
        # Load the image in greyscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # create a CLAHE object (Arguments are optional).
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img_out = clahe.apply(img_gray)
        if testing:
            cv2.imshow('Equalized', img_out)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return img_out