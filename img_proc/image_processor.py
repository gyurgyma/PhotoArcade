import cv2
import numpy


class ImageProcessor:

    def __init__(self, filepath="img_proc/mrkoolaid.jpg"):
        self.image = cv2.imread("img_proc/mrkoolaid.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

    def display_image(self, img):
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def find_contours(self, img=None):
        if img is None:
            ret, thresh = cv2.threshold(self.image, 127, 255, 0)
        else:
            ret, thresh = cv2.threshold(img, 127, 255, 0)
        self.display_image(thresh)
        print(thresh.dtype)

        im2, contours, hierarchy = cv2.findContours(self.image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.display_image(im2)
        cv2.drawContours(im2, contours, -1, (134, 0, 100), 3)
        self.display_image(im2)
