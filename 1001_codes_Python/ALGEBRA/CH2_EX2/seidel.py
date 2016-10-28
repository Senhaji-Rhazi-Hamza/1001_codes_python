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
def mat_mult(A,B): #defining the multiply matrix
  m = len(A)  
  n = len(A[0])
  n2 = len(B)
  assert(n==n2),"impossible to multiply revise number of lines and coloumns" 
  p = len(B[0])
  C = [[0 for col in range(p)] for row in range(m)]
  for i in range(m):
    for j in range(p):
      for k in range(n):
        C[i][j]+= A[i][k] * B[k][j]
  return C
##################################################################################
#################################################################################
def seidel(A,B): # Matrix A and vector B of Ax = B
  n = len(A)
  #P = [ [A[i][j] if(i <=j) else 0  for i in range(n) ] for j in range(n)]
  #F = [ [-A[i][j] if(i > j) else 0  for i in range(n) ] for j in range(n)]
  tol = 10 ** -5
  err = 10
  it = 0
  max_iter = 10000
  Un0 = [1 for i in range(n)]
  Un1 = [1 for i in range(n)]
  while ((err > tol) & (it < max_iter)):
    it = it + 1
    Un1 =[(1/A[i][i]) * (B[i] - sum(A[i][j] * Un0[j] if i > j  else (A[i][j] * Un1[j] if i < j  else 0 ) for j in range(n) )) for i in range(n)]
    #Un1 = [ (1/A[i][i]) * (B[i] - sum(A[i][j] *Un0[j] if(i!=j) else 0 for j in range(n) )) for i in range(n) ]
    #Un1 = [ (1/A[i][i]) * (B[i] - sum(A[i][j] if(i!=j) else 0 for j in range(n) )) for i in range(n) ]
    err = math.sqrt(sum([(Un0[i] - Un1[i])**2 for i in range(n)]))
    Un0 = Un1
  return Un1
##################################################################################
