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
cv2.imshow('zero image', result)

rho = 1  # разрешение расстояния в пикселях сетки Хафа
theta = numpy.pi / 180  # угловое разрешение в радианах сетки Хафа
threshold = 15  # минимальное количество голосов (пересечений в ячейке сетки Хафа)
min_line_length = 50  # минимальное количество пикселей, составляющих линию
max_line_gap = 20  # максимальный промежуток в пикселях между соединяемыми сегментами линии
image_lines = cv2.HoughLinesP(mask, rho, theta, threshold, numpy.array([]), min_line_length, max_line_gap)
print('image_lines', image_lines)

cv2.waitKey(0)
