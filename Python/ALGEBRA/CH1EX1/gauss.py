def gauss(Mat,b):
  n = len(Mat)
  m = len(b)
  x = [0 for y in range(n)]
  #k = 1
  for k in range (1,n):
    for i in range(k,n):
      for j in range(n):
        Mat[i][j] = Mat[i][j] - (Mat[i][k -1]  / Mat[k - 1][k -1])*Mat[k - 1][j]
  for i in reversed(range(n)):
    x[i] =  (b[i] - sum([Mat[i][j] * x[j] for j in range(i,n)]))/Mat[i][i]
#assertion = False
  #assert assertion, "erreur en entrée"
  
  return x
