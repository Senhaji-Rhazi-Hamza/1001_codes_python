import numpy as np
import math
def gradient(A,B):
  n = len(A) 
  #Un0 = [1 for i in range(n)] #initialize start vec
  Un1 = [1 for i in range(n)]
  err = 10
  tol = 10 ** -5
  it = 0
  max_iter = 10000
  while ((err > tol) & (it < max_iter)):
    it +=1
    r = - (np.dot(A,Un1) - B)
    alph = np.dot(r, r) / np.dot(r, np.dot(A, r))
    Un0 = Un1[:]
    Un1 = Un0 + alph * r
    err = math.sqrt(sum([(Un0[i] - Un1[i]) ** 2 for i in range(n)]))
  return Un1

