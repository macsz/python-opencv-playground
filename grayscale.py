import cv2
import matplotlib.pyplot as plt

image = cv2.imread('images/bird.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(image, cmap='gray', interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
