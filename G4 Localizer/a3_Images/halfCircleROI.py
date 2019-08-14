import cv2
import numpy
import math


def halfCircleROI(imageSize,radius, direction): 
    img = numpy.zeros(*imageSize)
    axes = (radius,radius)
    angle = 0
    startAngle = direction - math.pi/2
    endAngle = direction + math.pi/2
    center = (imageSize[0]/2,imageSize[1]/2)
    color = 255
    
    cv2.ellipse(img,center,axes,angle,startAngle,endAngle,color,thickness=-1)
    return img

#Documentation: see Github Wiki