import numpy as np
import cv2
import image as im
# Load an color image in grayscale

img = cv2.imread("ressources/cat.jpg",1)
name = "ressources/cat.jpg"

iobj = im.Image(name)
iobj.show(3)

