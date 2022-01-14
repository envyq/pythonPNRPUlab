import cv2

img = cv2.imread('template.png')
cv2.imshow('default image', img)
cv2.waitKey(0)