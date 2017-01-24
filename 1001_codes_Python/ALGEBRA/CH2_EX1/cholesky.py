import numpy as np
import math as mt
def cholesky(A,b):
  len_cols = len(A)
  n = len_cols
  return 0
def cholesky_get_l(A):
  
  n = len(A)
  L = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    for j in range(i+1):
      s = sum(L[i][k]*L[j][k] for k in range(j))
      L[i][j] = mt.sqrt(A[i][j] - s) if (i == j) else ((A[i][j] - s) / L[j][j] )
  return L
