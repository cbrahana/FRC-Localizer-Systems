import numpy
import cv2
import math

class IMAGE:
    def __init__(self,image,lens_radius):
        height,width = *image.shape
        radius = lens_radius
        height_center = height/2
        width_center = width/2
        return None