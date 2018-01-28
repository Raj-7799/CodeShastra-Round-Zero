import cv2

im = cv2.imread("known/Akshay.jpg")

im = cv2.resize(im, (1008, 756))

cv2.imwrite("Akshay.jpg", im)