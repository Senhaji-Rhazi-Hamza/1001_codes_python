import jacobi
import seidel
import gradient
import conjugate_gradient
#jacobi test

## range matrix
n = 5

############################Constructing matrix#####################################
A = [[ (5 * int(i == j) | -2 * (i == j + 1) | -2 * (j == i + 1)) for i in range (n)] for j in range(n)]
B = [ (i == n - 1) for i in range(n) ]
A[n - 1][n - 1] = 3
A[1][1] = 4
############################Constructing matrix#####################################

#jacobi test
print("jacobi result ",jacobi.jacobi(A,B),"\n")

############################Constructing matrix#####################################
A = [[ (5 * int(i == j) | -2 * (i == j + 1) | -2 * (j == i + 1)) for i in range (n)] for j in range(n)]
B = [ (i == n - 1) for i in range(n) ]
A[n - 1][n - 1] = 3
A[1][1] = 4
############################Constructing matrix#####################################

#seidel test
print("seidel result ",seidel.seidel(A,B),"\n")

############################Constructing matrix#####################################

A = [[ (5 * int(i == j) | -2 * (i == j + 1) | -2 * (j == i + 1)) for i in range (n)] for j in range(n)]
B = [ (i == n - 1) for i in range(n) ]
A[n - 1][n - 1] = 3
A[1][1] = 4
############################Constructing matrix#####################################

#gradient test
print("gradient result ",gradient.gradient(A,B),"\n")
############################Constructing matrix#####################################

A = [[ (5 * int(i == j) | -2 * (i == j + 1) | -2 * (j == i + 1)) for i in range (n)] for j in range(n)]
B = [ (i == n - 1) for i in range(n) ]
A[n - 1][n - 1] = 3
A[1][1] = 4
############################Constructing matrix#####################################

#conjugate_gradient test
print("conjugate_gradient result ",conjugate_gradient.conjugate_gradient(A,B),"\n")
