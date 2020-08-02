import cv2
import numpy as np
# for pick image from images
img = cv2.imread('Resources/card.jpg')

width, height = 1600, 494
pts1 = np.float32([[39,339], [45,937], [453,339], [451,619]])
pts2 = np.float32([[0, 0], [width,0], [0,height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)
