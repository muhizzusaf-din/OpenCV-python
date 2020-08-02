import cv2
# for resize: width, height
img = cv2.imread('Resources/nayeon2.jpg')
print(img.shape)

imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

# for cropping image
# heigth, width
imgCrop = img[150:250,98:134]

cv2.imshow("Image", img)
# cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCrop)
cv2.waitKey(0)
