import cv2
import numpy


class ImageProcessor:

    def __init__(self, filepath="img_proc/mrkoolaid.jpg"):
        self.image_original = cv2.imread(filepath)
        # self.display_image(self.image_original)
        self.image = cv2.cvtColor(self.image_original, cv2.COLOR_RGB2GRAY)
        # self.display_image(self.image)

    def display_image(self, img):
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def find_contours(self, img=None):
        if img is None:
            ret, thresh = cv2.threshold(self.image, 150, 255, 0)
        else:
            ret, thresh = cv2.threshold(img, 150, 255, 0)
        # self.display_image(thresh)

        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.image_original, contours, -1, (134, 0, 100), -1)
        # self.display_image(self.image_original)
        # print(self.image_original)

    @property
    def terrain(self):
        return None

    def chomp_field(self, center, radius: float):
        pass
