#################################################################################
def mat_mult(A,B): #defining the multiply matrix
  n = len(A)  
  m = len(B[0])
  C = [[0 for i in range(n)] for j in range(m)]
  for i in range(n):
    for j in range(m):
      for k in range(m):
        C[i][j]+= A[i][k] * B[k][j]
  return C
##################################################################################
#################################################################################
def jacobi(A,B): # Matrix A and vector B of Ax = B
  n = len(A)
  D = [ [A[i][j] if(i==j) else 0  for i in range(n) ] for j in range(n)]
  E = [ [-A[i][j] if(i < j) else 0  for i in range(n) ] for j in range(n)]
  F = [ [-A[i][j] if(i > j) else 0  for i in range(n) ] for j in range(n)]
  Un0 = [1 for i in range(n)]
  Un1 = [1 for i in range(n)]
#  print(D)
#  print(E)
#  print(F)
  return 9
##################################################################################
