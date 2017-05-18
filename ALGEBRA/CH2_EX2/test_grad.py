import numpy as np
def conjugate_gradient2(A,B):
  n = len(A)
  Un1 = [0 for i in range(n)] #initialize start vec
  r = (B - np.dot(A, Un1))
  X = r + Un1
  Y = np.dot(X, -1)
  return Y
