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
def gauss(Matt,bb):
  n = len(Matt)
  m = len(Matt[0])
  mi =[0 for i in range(n)]
  perm_mat = [[int(i==j) for i in range(n)] for j in range(n)]
  Mat = [[val for val in liste] for liste in Matt]
  b = [bb[i] for i in range(n)]
  x = [0 for y in range(n)]
  index = 0
  maxx = int(Mat[0][0])
  for k in range (1,n):
###################################################################################
   #Looking for the max pivot, i could do it without that block of instruction 
    maxx = int(Mat[k-1][k-1])
    for r in range(k - 1,n):  
      if( Mat[r][k-1] > maxx): 
        maxx = int(Mat[r][k-1])
        index = r
    if (maxx != Mat[k-1][k-1]):
      perm_mat = [[int(i==j) for i in range(n)] for j in range(n)]
      perm_mat[k-1],perm_mat[index] = perm_mat[index],perm_mat[k-1]
      Mat = mat_mult(perm_mat,Mat)
      b[k-1],b[index] = b[index],b[k-1]
###################################################################################
    if(maxx == 0) : continue #if you havent find any pivot != 0
      #move to the next colone
    for i in range(k,n):
      mi[i] =  (Mat[i][k-1]  / Mat[k - 1][k -1]) 
      for j in range(n):
        p = Mat[i][j]
        Mat[i][j] = p -  Mat[k - 1][j] * mi[i] 
      b[i] = b[i] - b[k-1] * mi[i] 
    mi =[0 for i in range(m)]

  for i in reversed(range(n)):
    s = sum([Mat[i][j] * x[j] for j in range(i,n)])
    if(Mat[i][i] != 0):
      x[i] =  (b[i] - s)/Mat[i][i]
    else:
      x[i] = 0
  return x
###################################################################################
#assertion = False
  #assert assertion, "erreur en entrée"
  
def gauss2(AA,b):
  A = [[val for val in liste] for liste in AA]
  n = len(A)
  m = len(A[0])
  X = []
  for k in range(0,n-1):
    for i in range(k+1,n):
      m = A[i][k] / A[k][k]
      for j in range(k,n):
        A[i][j] = A[i][j] -m * A[k][j]
      b[i]=b[i] - m * b[k]
  X.append(b[n-1]/A[n-1][n-1])
  for i in range(n-2,-1,-1):
    s = 0
    for k in range(i+1,n):
      s+=A[i][k]*X[n-k-1]
    X.append((b[i] - s) / A[i][i])
  X.reverse()
  return X 
