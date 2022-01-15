import cv2
import numpy
import math

defaultImage = cv2.imread('template.png')
cv2.imshow('default image', defaultImage)
# hsv
defaultImage = cv2.cvtColor(defaultImage, cv2.COLOR_BGR2HSV)

maskLow = cv2.inRange(defaultImage, (0, 50, 20), (5, 255, 255))
maskUp = cv2.inRange(defaultImage, (175, 50, 20), (180, 255, 255))
mask = cv2.bitwise_or(maskLow, maskUp)

# creating a blank to draw
result = numpy.copy(defaultImage) * 0
cv2.imshow('mask image', mask)

rho = 1  # разрешение расстояния в пикселях сетки Хафа
theta = numpy.pi / 180  # угловое разрешение в радианах сетки Хафа
threshold = 15  # минимальное количество голосов (пересечений в ячейке сетки Хафа)
min_line_length = 50  # минимальное количество пикселей, составляющих линию
max_line_gap = 20  # максимальный промежуток в пикселях между соединяемыми сегментами линии
image_lines = cv2.HoughLinesP(mask, rho, theta, threshold, numpy.array([]), min_line_length, max_line_gap)

_length, _x1, _y1, _x2, _y2 = -1, -1, -1, -1, -1

for image_line in image_lines:
    for x1, y1, x2, y2 in image_line:
        length = math.sqrt(math.pow(int(x2) - int(x1), 2) + math.pow(int(y2) - int(y1), 2))
        if length > _length: _length, _x1, _y1, _x2, _y2 = length, x1, y1, x2, y2

destination = cv2.line(result, (_x1, _y1), (_x2, _y2), (255, 0, 0), 5)


# Вычисляем уравнение прямой
k = (_y1 - _y2) / (_x1 - _x2)
b = _y2 - k * _x2

print(f"Line equation: y = {-1 * round(k, 2)}*x + {int(b)}")

cv2.imshow('destination', destination)

cv2.waitKey(0)
