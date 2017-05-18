import math
#################################################################################
def mat_add(A,B): #defining addition matrix
  n = len(A[0])
  m = len(A)
  C = [[0 for i in range(n)] for j in range(m)]
  for i in range(n):
    for j in range(m):
      C[j][i] = A[j][i] + B[j][i]
  return C
##################################################################################
#################################################################################
def jacobi(A,B): # Matrix A and vector B of Ax = B
  n = len(A)
  D = [ [A[i][j] if(i==j) else 0  for i in range(n) ] for j in range(n)]
  E = [ [-A[i][j] if(i < j) else 0  for i in range(n) ] for j in range(n)]
  F = [ [-A[i][j] if(i > j) else 0  for i in range(n) ] for j in range(n)]
  tol = 10 ** -5
  err = 10
  it = 0
  max_iter = 10000
  Un0 = [1 for i in range(n)]
  Un1 = [1 for i in range(n)]
  while ((err > tol) & (it < max_iter)):
    it = it + 1
    #Un1 = [ (1/A[i][i]) * (B[i] - sum(A[i][j] if(i!=j) else 0 for j in range(n) )) for i in range(n) ]
    Un1 = [ (1/A[i][i]) * (B[i] - sum(A[i][j] *Un0[j] if(i!=j) else 0 for j in range(n) )) for i in range(n) ]
    err = math.sqrt(sum([(Un0[i] - Un1[i])**2 for i in range(n)]))
    Un0 = Un1
  return Un1
##################################################################################
