import cv2
import numpy


class ImageProcessor:

    def __init__(self, filepath):
        self._terrain = None
        self.image_original = cv2.imread(filepath)
        self._alpha = self.generate_alpha_image(self.image_original)
        # self.display_image(self.image_original)
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
        # self.display_image(thresh)

        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.image_original, contours, -1, self.contour_color, -2)
        # self.display_image(self.image_original)
        # print(self.image_original)

    def generate_terrain(self):
        """Generates terrain 2d array, now with alpha generation too!"""
        rows = len(self.image_original)
        cols = len(self.image_original[0])
        self._terrain = [[0] * cols for i in range(rows)]
        for i in range(rows):
            self._terrain[i] = [0] * cols
        self.display_image(self.image_original)
        for row in range(rows):
            for col in range(cols):
                (r, g, b) = self.image_original[row, col]
                if (r, g, b) == self.contour_color:
                    self._terrain[row][col] = 0
                    self._alpha[row][col][3] = 0
                else:
                    self._terrain[row][col] = 1
                    self._alpha[row][col][3] = 200

    def generate_alpha_image(self, img):
        """generates alpha image from rgb"""
        b, g, r = cv2.split(img)
        alpha_channel = numpy.zeros(b.shape, dtype=b.dtype)
        alpha_channel = alpha_channel.astype(numpy.uint8)
        return cv2.merge((b, g, r, alpha_channel))
        #return numpy.array((b, g, r, alpha_channel))

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
        print(center)
        """Remove a circular section"""
        x, y = center
        radius = int(radius)
        for row in range((y - radius), (y + radius)):
            for col in range((x - radius), (x + radius)):
                if (x < 0) or (x >= len(terrain[row])):
                    continue
                if (y < 0) or (y >= len(terrain)):
                    continue
                dist = numpy.sqrt(((col - x)**2) + ((row - y)**2))
                if dist > radius:
                    continue
                if self.valid_terrain_access(row, col):
                    print(row, col)
                    if self.terrain[row][col] == 1:
                        self.terrain[row][col] = 0

    def display_terrain(self):
        # This should convert the terrain to an image (for debugging purposes).
        rows = len(self._terrain)
        cols = len(self._terrain[0])
        test_matrix = numpy.array(self.image_original)
        for row in range(rows):
            for col in range(cols):
                #print(self._terrain[row][col])
                if self._terrain[row][col] is 1:
                    test_matrix[row][col] = [0, 0, 0]
                else:
                    test_matrix[row][col] = [255, 255, 255]

        self.display_image(test_matrix)

    def display_alpha(self):
        self.display_image(self.display_alpha)
