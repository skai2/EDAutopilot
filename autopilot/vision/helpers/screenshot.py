import d3dshot
import numpy

def screenshot(x_left, y_top, x_right, y_bot):
    """Gets screenshot specified by given coordinates"""
    d = d3dshot.create(capture_output="numpy")
    d.screenshot()