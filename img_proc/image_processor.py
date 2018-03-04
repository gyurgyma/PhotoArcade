import cv2
import numpy


class ImageProcessor:

    def __init__(self, filepath="img_proc/mrkoolaid.jpg"):
        self._terrain = None

        self.image_original = cv2.imread(filepath)
        # self.display_image(self.image_original)
        self.work_image = cv2.cvtColor(self.image_original, cv2.COLOR_RGB2GRAY)
        self.contour_color = (134, 0, 100)
        self._terrain = None

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
                else:
                    self._terrain[row][col] = 1

        return self._terrain

    @terrain.setter
    def terrain(self, new_terrain):
        self._terrain = new_terrain

    def chomp(self, center, radius: float):
        """Remove a circular section"""
        x, y = center
        radius = numpy.floor(radius)
        terrain_cp = self.terrain
        for row in range((y - radius), (y + radius)):
            for col in range((x - radius), (x + radius)):
                dist = numpy.sqrt(((col - x)**2) + ((row - y)**2))
                if dist > radius:
                    continue
                if terrain_cp[row][col] == 1:
                    terrain_cp[row][col] = 0
        
        self.terrain = terrain_cp

    def display_terrain(self):
        # This should convert the terrain to an image (for debugging purposes).  It doesn't work yet
        rows = len(self._terrain)
        cols = len(self._terrain[0])
        test_array = [[0] * cols for i in range(rows)]
        for i in range(rows):
            test_array[i] = [(1, 0, 1)] * cols

        for row in range(rows):
            for col in range(cols):
                #print(self._terrain[row][col])
                if self._terrain[row][col] is 1:
                    test_array[row][col] = (0, 0, 0)
                else:
                    test_array[row][col] = (255, 255, 255)
        #self.display_image(numpy.array(test_array))
