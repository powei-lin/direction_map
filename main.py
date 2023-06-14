import numpy as np
import cv2

def direction_map(h: int, w: int):
    x = np.linspace(0, w, w, endpoint=False)
    y = np.linspace(0, h, h, endpoint=False)
    xv, yv = np.meshgrid(x, y)
    cx = w / 2 - 0.5
    cy = h / 2 - 0.5
    xv -= cx
    yv -= cy
    rv = np.sqrt(xv*xv + yv*yv)
    img = np.dstack((127*np.ones((h, w)), 127+127*xv/rv, 127+127*yv/rv)).astype(np.uint8)
    return img

a = direction_map(1080, 1920)
cv2.imwrite("dirmap.png", a)