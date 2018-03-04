import cv2
import numpy


class ImageProcessor:

    def __init__(self, filepath="img_proc/mrkoolaid.jpg"):
        self._terrain = None

        self.image_original = cv2.imread(filepath)
        # self.display_image(self.image_original)
        self.work_image = cv2.cvtColor(self.image_original, cv2.COLOR_RGB2GRAY)
        self.contour_color = (134, 0, 100)

    def display_image(self, img):
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def find_contours(self, img=None):
        if img is None:
            ret, thresh = cv2.threshold(self.work_image, 150, 255, 0)
        else:
            ret, thresh = cv2.threshold(img, 150, 255, 0)
        self.display_image(thresh)

        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.image_original, contours, -1, self.contour_color, -2)
        self.display_image(self.image_original)
        # print(self.image_original)

    @property
    def terrain(self):
        # rows = len(self.work_image[0])
        # print(rows)
        # cols = len(self.work_image)
        # print(cols)
        # terrain = [(0 * cols) for row in range(rows)]
        # print(terrain)
        # for col in self.work_image:
        #     for row in self.work_image[col]:
        #         if self.work_image[col][row] is self.contour_color:
        #             terrain[col][row] = 0
        #         else:
        #             terrain[col][row] = 1
        #
        return self._terrain

    @terrain.setter
    def terrain(self, new_terrain):
        self._terrain = new_terrain



    def chomp(self, center, radius: float):
        """Remove a circular section"""
        pass

    def display_terrain(self):
        rows = len(self.work_image[0])
        # print(rows)
        # cols = len(self.work_image)
        # print(cols)
        # terrain_test = [(0 * cols) for row in range(rows)]
        # print(self.terrain)
        # for col in self.terrain:
        #     for row in self.terrain[col]:
        #         if self.work_image[col][row] is self.contour_color:
        #             terrain_test[col][row] = 0
        #         else:
        #             terrain_test[col][row] = 1
