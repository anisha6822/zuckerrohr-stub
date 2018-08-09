'''
Code based on zuckerrohr-stub

Copyright (C) 2018  Udit kumar Agarwal <dev.madaari@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# using Hough Transform

import cv2
import numpy as np
from matplotlib import pyplot as plt


def caminit(img):
    print(len(img)) # Width of pic
    print(len(img[0])) # Height of pic
    return cv2.resize(img[100:600,150:510], (200,200), interpolation = cv2.INTER_AREA)

def invert_color(frame):
    return 255-frame
    
def plt_img(img):
    plt.imshow(img)

img = cv2.imread('../images/img1.jpeg')
img = caminit(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mini = maxi = 0
offset = 10
edges = cv2.Canny(gray, 150, 200, apertureSize = 3)
lines = cv2.HoughLinesP(edges, 1, np.pi/2, 10, None, 2, 1);
for line in lines[0]:
    pt1 = (line[0],line[1])
    pt2 = (line[2],line[3])
    angle = np.arctan2(line[0] - line[2], line[1] - line[3]) * 180.0 / np.pi
    if abs(angle) == 90:
        continue
    if (line[0] < mini) or (mini == 0):
        mini = line[0]
    if line[0] > maxi:
        maxi = line[0]
cv2.line(img, (mini - offset,0), (mini - offset,200), (0,0,255), 1)
cv2.line(img, (maxi + offset,0), (maxi + offset,200), (0,0,255), 1)
plt_img(img)
cv2.destroyAllWindows()
