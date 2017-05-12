import numpy as np
import cv2

class Image:
  #self.s = None 
  def __init__(self, name):
      self.img = cv2.imread(name,1)
      height, width = self.img.shape[:2]
      self.scales = None
      self.size = min(height, width)
      self.img = cv2.resize(self.img,(self.size, self.size), interpolation = cv2.INTER_CUBIC)
  def show(self):
    cv2.imshow('image',self.img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  def set_scales(self):
    if self.scales is None:
      self.scales = [cv2.resize(self.img,None,fx= 2**-(i), fy=2**-(i), interpolation = cv2.INTER_CUBIC)  for i in range(int(np.log2(self.size)))]
  def show(self, scale):
      if self.scales is None:
        self.set_scales()
      cv2.imshow('image',self.scales[scale])
      cv2.waitKey(0)
      cv2.destroyAllWindows()
  def show_last(self):
    if self.scales is None:
      self.set_scales()
    self.show(len(self.scales) - 1)

