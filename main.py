import cv2
import numpy

defaultImage = cv2.imread('template.png')
cv2.imshow('default image', defaultImage)
# hsv
lowSide = numpy.array([49, 41, 218])
upSide = numpy.array([100, 100, 255])

mask = cv2.inRange(defaultImage, lowSide, upSide)
cv2.imshow('mask iamge', mask)

cv2.waitKey(0)
