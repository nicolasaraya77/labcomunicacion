import cv2
import time 
if __name__ == '__main__':
    dec = cv2.imread("IMG_0108.JPG")
    cv2.imwrite("IMG_0108_recompressed.png", dec)
