import d3dshot
import numpy

_d3d = d3dshot.create(capture_output="numpy")


def screenshot(left, top, right, bottom):
    """Gets screenshot specified by given coordinates"""
    left, top, right, bottom = round(left), round(top), round(right), round(bottom)
    # _d3d,create above has output set to numpy but it doesn't seem to care :/ output is pil
    pil_image = _d3d.screenshot(region=(left, top, right, bottom))
    # So need to convert to cv2 numpy array
    numpy_image = numpy.array(pil_image)
    return numpy_image


if __name__ == '__main__':
    print(screenshot(100.5, 100, 300, 300))
    print(_d3d.display)
