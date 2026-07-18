from skimage import data
import cv2

image = data.camera()

cv2.imwrite("examples/sample.png", image)

print("Sample image created: examples/sample.png")