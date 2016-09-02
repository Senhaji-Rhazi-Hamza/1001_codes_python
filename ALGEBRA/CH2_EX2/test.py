import jacobi
#jacobi test
####################################################################
A = [ [(i + j) for i in range(5) ] for j in range(5)]
B = [1 for i in range(5) ]
jacobi.jacobi(A,B)
