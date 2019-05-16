import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny_image(img):
    image = cv2.imread(img)
    lane_image = np.copy(image)

    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)

    return canny


image = canny_image('img/img_1.jpg')

plt.imshow(image)
plt.show()
