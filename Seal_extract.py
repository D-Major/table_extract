import cv2
import numpy as np

np.set_printoptions(threshold=np.inf)
image=cv2.imread("table3.jpg")

hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
low_range = np.array([150, 30, 100])
high_range = np.array([180, 255, 225])
th = cv2.inRange(hue_image, low_range, high_range)
index1 = th == 255

img = np.zeros(image.shape, np.uint8)
img[:, :] = (255,255,255)
img[index1] = image[index1]#(0,0,255)
# cv2.imshow('original_img', image)
cv2.imshow('extract_img', img)
cv2.waitKey(3000)