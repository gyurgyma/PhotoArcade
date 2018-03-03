import cv2
from img_proc import image_processor

img_proc = image_processor.ImageProcessor()
#img_proc.display_image()
img_proc.find_contours(img_proc.image)


