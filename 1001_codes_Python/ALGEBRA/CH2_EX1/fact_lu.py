import numpy as np
# L U Factorization Gauss
def fact_lu(Mat,b):
  n = len(Mat)
  m = len(b)
  x = [0 for y in range(n)]
  L = [[float(i == j) for i in range(n)] for j in range(n)]
  #L is the Lower triangular Matrix
  for k in range (1,n):
    for i in range(k,n):
      for j in range(n):
        L[i][j] = Mat[i][k -1]  / Mat[k - 1][k -1]
        Mat[i][j] = Mat[i][j] - (Mat[i][k -1]  / Mat[k - 1][k -1])*Mat[k - 1][j]
  return [L,Mat]



#that 2nd solution take on accout if the pivot is equal to 0
###########################################################
def mat_permut(i,j,n):
  P = [[float(i == j) for i in range(n)] for j in range(n)]
  P[i], P[j] = P[j], P[i]
  return P
###########################################################
###########################################################
def fact_lu_piv(Mat,b):
  n = len(Mat)
  m = len(b)
  x = [0 for y in range(n)]
  L = [[float(i == j) for i in range(n)] for j in range(n)]
  #L is the Lower triangular Matrix
  for k in range (1,n):
    for i in range(k,n):
      for j in range(n):
        if(Mat[k - 1][k -1] == 0) : 
          maxindex = k - 1
          for r in range(k - 1,n - 1):
            if (Mat[r + 1][r + 1] > Mat[r][r]):
              maxindex = r + 1
          P = mat_permut(k - 1,maxindex,n)
          np.dot(Mat,P)  
        L[i][j] = Mat[i][k -1]  / Mat[k - 1][k -1]
        Mat[i][j] = Mat[i][j] - (Mat[i][k -1]  / Mat[k - 1][k -1])*Mat[k - 1][j]
  return [L,Mat]
###########################################################
def solv_lu(L,U,b):
  n = len(b)
  #Y = [1/L[i][i] *(b[i] - sum([(L[i][j] * Y[j]) for j in range(i-1)]) for i in range(n)]
  
  Y = [1/L[i][i] * (b[i] - sum([(L[i][j] * Y[j]) for j in range(i-1)])) if L[i][i] != 0 else 0 for i in range(n)]
  X = [1/U[i][i] * (b[i] - sum([(L[i][j] * Y[j]) for j in range(i+1,n)])) if U[i][i] != 0 else 0 for i in reversed(range(n))]
  return X
