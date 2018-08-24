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

# using Contour detection

import cv2
import numpy as np
from matplotlib import pyplot as plt


def caminit(img):
    print(len(img)) # Width of pic
    print(len(img[0])) # Height of pic
    print(img.type())
    return cv2.resize(img[100:600,150:510], (200,200), interpolation = cv2.INTER_AREA)

def invert_color(frame):
    return 255-frame
    
def plt_img(img):
    plt.imshow(img)

img = cv2.imread('../images/img1.jpeg')
img = caminit(img)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);

#ret,thresh = cv2.threshold(img,127,255,0)
#contours,hierarchy = cv2.findContours(thresh, 1, 2)
#cv2.drawContours(img,contours,-1,(0,255,0),3);
plt_img(img)
cv2.destroyAllWindows()
