import cv2
import numpy

defaultImage = cv2.imread('template.png')
cv2.imshow('default image', defaultImage)
# hsv
lowSide = numpy.array([49, 41, 218])
upSide = numpy.array([100, 100, 255])
# creating a blank to draw
result = numpy.copy(defaultImage) * 0
mask = cv2.inRange(defaultImage, lowSide, upSide)
cv2.imshow('mask image', mask)
cv2.imshow('zero ia=mge', result)

cv2.waitKey(0)
