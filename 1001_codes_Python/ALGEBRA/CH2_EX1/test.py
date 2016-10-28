import gauss
import fact_lu
import matplotlib.pylab as plt
import numpy as np
# gauss function test#
A = [[1,3,1],[1,-2,-1],[2,1,2]]
B = [10,-6,10]
n = len(A)
X = gauss.gauss(A,B)
print("solution value with gauss method\n ",X)
# gauss function test#



# comparing solution of our circuit problem with gauss method and analytic method test#


n = 20
E = 12
R = 50
io = E / R

Xanalytic = []

Matrix = [[float(4 * (i == j) - 1 *(( i== j + 1 ) or (i == j - 1))) for i in range(n)] for j in range(n)]
Matrix[n-1][n-1] = 3
B = [int(i==0) for i in range(n)]
Xgauss = [0 for i in range(n)]
N = [i for i in range(n)] 
for i in range(1,n+1):
  xk = (2 - np.sqrt(3))**i
  Xanalytic.append(xk)
 
Xgauss = gauss.gauss(Matrix,B)
#transform in log10 for plot purpuse

XlogAnalytic = [np.log10(Xanalytic[i]) for i in range(n)]
Xloggauss = [np.log10(Xgauss[i]) for i in range(n)]

plt.plot(N,Xloggauss,'b:',label="numeric solution")
plt.plot(N,XlogAnalytic,'r--',label="analytic solution")
plt.xlabel("rank ith current ")
plt.ylabel("log10(ik)")
plt.legend()
plt.show()
