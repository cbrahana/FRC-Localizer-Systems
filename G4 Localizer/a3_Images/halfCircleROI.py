import cv2
import numpy
import math


def halfCircleROI(IMAGE_in, direction):  
    img = numpy.zeros(IMAGE_in.height,IMAGE_in.width)
    axes = (IMAGE_in.radius,IMAGE_in.radius)
    angle = 0
    startAngle = direction - math.pi/2
    endAngle = direction + math.pi/2
    center = (IMAGE_in.height/2,IMAGE_in.width/2)
    color = 255
    
    cv2.ellipse(img,center,axes,angle,startAngle,endAngle,color,thickness=-1)
    return img

#Documentation: see Github Wiki