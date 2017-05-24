import cv2
import matplotlib.pyplot as plt

image = [
    cv2.imread('images/bird.jpg', cv2.IMREAD_COLOR),
    cv2.imread('images/bird.jpg', cv2.IMREAD_GRAYSCALE)
]

i = 0
while True:
    plt.imshow(image[i % (len(image))], cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.pause(1)
    i += 1
    if i > 10:
        break
