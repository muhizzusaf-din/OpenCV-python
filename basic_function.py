import cv2
import numpy as np

img = cv2.imread('Resources/nayeon.jpg')
kernel = np.ones((5,5),np.uint8)


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(3,3),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("Eroded Image of pretty nayeon", imgEroded)
cv2.imshow("Canny Image of pretty nayeon", imgCanny)
cv2.imshow("Gray Image of pretty nayeon", imgGray)
cv2.imshow("Blur Image of pretty nayeon", imgBlur)
cv2.imshow("Dialation Image of pretty nayeon", imgDialation)
cv2.waitKey(0)