import cv2
import numpy
import os


class ImageProcessor:

    def __init__(self, filepath):
        self._terrain = None
        self.terrain_display_count = 0
        self.im_name = ""

        self.image_original = cv2.imread(filepath)
        self.backup_images = numpy.array(self.image_original, copy=True)
        self.generate_alpha_image(self.image_original)
        self.work_image = cv2.cvtColor(self.image_original, cv2.COLOR_RGB2GRAY)
        self.contour_color = (134, 0, 100)
        self.find_contours()
        self.generate_terrain()

    def display_image(self, img):
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def find_contours(self, img=None):
        if img is None:
            ret, thresh = cv2.threshold(self.work_image, 150, 255, 0)
        else:
            ret, thresh = cv2.threshold(img, 150, 255, 0)
        median = cv2.medianBlur(thresh, 9)

        im2, contours, hierarchy = cv2.findContours(median, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.image_original, contours, -1, self.contour_color, -1)

    def generate_terrain(self):
        """Generates terrain 2d array, now with alpha generation too!"""
        rows = len(self.image_original)
        cols = len(self.image_original[0])
        self._terrain = [[0] * cols for i in range(rows)]
        for i in range(rows):
            self._terrain[i] = [0] * cols
        if self._alpha is None:
            self.generate_alpha_image(self.backup_images)
        for row in range(rows):
            for col in range(cols):
                (r, g, b) = self.image_original[row, col]
                if (r, g, b) == self.contour_color:
                    self._terrain[row][col] = 0
                    self._alpha[row][col][3] = 150
                else:
                    self._terrain[row][col] = 1
                    self._alpha[row][col][3] = 255

    def generate_alpha_image(self, img):
        """generates alpha image from rgb"""
        rows = len(self.image_original)
        cols = len(self.image_original[0])
        self._alpha = [[0] * cols for i in range(rows)]
        for i in range(rows):
            self._alpha[i] = [(0, 0, 0, 200)] * cols
        (b, g, r) = cv2.split(img)
        for row in range(rows):
            for col in range(cols):
                self._alpha[row][col] = (b[row][col], g[row][col], r[row][col], 255)

        self._alpha = numpy.array(self._alpha)
        self.write_alpha_image()

    @property
    def terrain(self):
        return self._terrain

    @terrain.setter
    def terrain(self, new_terrain):
        self._terrain = new_terrain

    def valid_terrain_access(self, row, col):
        if row <= 0 or col <= 0:
            return False
        elif row >= len(self.terrain) or col >= len(self.terrain[0]):
            return False
        else:
            return True

    def chomp(self, center, radius: float):
        """Remove a circular section"""
        x, y = (int(center[0]), int(center[1]))
        radius = int(radius)
        len(self._terrain)
        if self._alpha is None or self._terrain is None:
            self.generate_terrain()
        for row in range((y - radius), (y + radius)):
            for col in range((x - radius), (x + radius)):
                dist = numpy.sqrt(((col - x)**2) + ((row - y)**2))
                if dist > radius:
                    continue
                if not self.valid_terrain_access(row, col):
                    continue
                self._terrain[row][col] = 0
                self._alpha[row][col][0] = 255
                self._alpha[row][col][1] = 255
                self._alpha[row][col][2] = 255

        self.write_alpha_image()

    def display_terrain(self):
        # This should convert the terrain to an image (for debugging purposes).
        rows = len(self._terrain)
        cols = len(self._terrain[0])
        test_matrix = numpy.array(self.image_original)
        for row in range(rows):
            for col in range(cols):
                if self._terrain[row][col] is 1:
                    test_matrix[row][col] = [0, 0, 0]
                else:
                    test_matrix[row][col] = [255, 255, 255]

    def write_alpha_image(self):
        if self.terrain_display_count > 0:
            os.remove(self.im_name)

        self.im_name = "terrain" + str(self.terrain_display_count) + ".png"
        self.terrain_display_count += 1
        cv2.imwrite(self.im_name, self._alpha)
