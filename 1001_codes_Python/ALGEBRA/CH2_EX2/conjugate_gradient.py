import numpy as np
import math
def conjugate_gradient(A,B):
  n = len(A)
  Un1 = [0 for i in range(n)] #initialize start vec
  r = (B - np.dot(A, Un1))
  pi1 = r
  err = 10
  tol = 10 ** -5
  it = 0
  max_iter = 10000
  while ((err > tol) & (it < n  )):
    Un0 = Un1[:]
    alph =  np.dot(r,r) / np.dot(pi1, np.dot(A,pi1))
    Un1 = Un0 + np.dot(alph, pi1)
    r1 = (r - np.dot(alph,np.dot(A, pi1)))
    beta =  np.dot(r1,r1) / np.dot(r,r) 
    pi1 = r1 + beta * pi1
    r = r1
    it +=1
    err = math.sqrt(sum([(Un0[i] - Un1[i]) ** 2 for i in range(n)]))
  return Un1




