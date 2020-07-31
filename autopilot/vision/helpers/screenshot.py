import d3dshot
import numpy

d = d3dshot.create(capture_output="numpy")


def screenshot(left, top, right, bottom):
    """Gets screenshot specified by given coordinates"""
    return d.screenshot(region=(left, top, right, bottom))

if __name__ == '__main__':
    print(screenshot(100,100,300,300))
    print(d.display)
    resolution = d.display.resolution
    print(resolution[0])