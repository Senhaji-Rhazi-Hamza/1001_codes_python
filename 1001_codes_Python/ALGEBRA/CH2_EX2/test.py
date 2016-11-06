import jacobi
import seidel
import gradient
#jacobi test
####################################################################
n = 5
A = [ [1 if (i!= j) else n+1 for i in range(n) ] for j in range(n)]
B = [1 for i in range(n) ]
A = [[3,-1,-1],[-1,3,1],[2,1,4]]
B = [1,3,7]
#xjacobi expected = [1,1,1]
print("jacobi result ",jacobi.jacobi(A,B),"\n")
A = [[3,-1,-1],[-1,3,1],[2,1,4]]
B = [1,3,7]
print("seidel result ",seidel.seidel(A,B),"\n")
A = [[1,1,1],[1,3,1],[1,1,1]]
B = [2,1,1]
print("gradient result ",gradient.gradient(A,B),"\n")
