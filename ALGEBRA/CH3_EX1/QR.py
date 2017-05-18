import numpy as np
import math as math
#######################################
def normalize(U):
  norm = np.linalg.norm(U)
  U = U / norm
  return U
#######################################
def orthonormalise_base(B):
  n = len(B)
  Ba = np.array(B)
#Ba is the base given transformed to an array if is'nt already
  P = []
  for i in range (n):
    vec = np.sum([np.dot(np.dot(Ba[i], P[k]), P[k]) for k in range(i)], 0)
    V = Ba[i] - vec
    V = normalize(V)
    P.append(V)
  return P
def fact_qr(A):
  n = len(A)
  base_A = np.array(A) #transformin A to an array for numpy use purpuse
  base_A = base_A.transpose() 
#for me A[i] is the line, not the colone
#so i should get the colone what i do with A.transpose()
#Q is the orthonormalized base got from the base A(u1,..,un)
  Q = np.array(orthonormalise_base(base_A))
  R = [[(np.dot(Q[i],base_A[j]) if (i <= j) else 0)  for j in range(n)] for i in range(n)]
  return Q.transpose() ,R
def diagonalise_QR(A):
  tol = 10 ** -3
  e = 1 + tol
  ref = np.linalg.norm(A)
  T0 = A
  n = len(A)
  while (e > tol):
    Q,R = fact_qr(T0)
    Q = np.array(Q)
    T1 = np.dot(Q.transpose(), np.dot(T0, Q))
    T0 = T1
    S = [[T1[i][j]**2 if i > j else 0 for i in range(n)] for j in range(n)]
#constructing a matrix triangular inferior
    e = sum([math.sqrt(sum(S[i])) for i in range(n)])
#e is a sort of norm which will tend to--> 0 where T1 will becam triangular
  Lymi = [T1[i][i] for i in range(n)]
  return Lymi

