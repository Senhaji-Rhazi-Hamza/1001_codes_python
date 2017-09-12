######################################################################
######################################################################
Explanation of gauss method


A : matrix belong to MnR 
X : Vector n dimension that we try to find
B : vector known

system   Ax = B

##Start solving

the idea is to transform the system with linears combinations to obtain 
another system Ux = C, this system have the same asolution as Ax=B
but in this system U is a triangular matrix inferior or superior 
we prefer to choose it superior here
the system become something liket that 

a11*x1 + a12*x2 + ........+ a1n*xn = c1
       + a22*x2 + ........+ a2n*xn = c2
                + ........+ a3n*xn = c3
                     .
                     .
                     .
                     .
                     .
                            ann*xn = cn


it become easy to solve starting from solving xn

xi = (ci - sum( aij * xj)) / aii   | from j = 1 to i - 1
#####################################################################
##2-Jacobi Method

let imagine we have a system writen Ax = b 

A : matrix belong to MnR symetric and Diagonal strict(means |aii| > sum(aij) with i!=j)
X : Vector n dimension that we try to find
b : vector known

##Start solving

so let decompose A = D - E - F

D : Diagonal matrix
E : Triangular inferior Matrix
F : Triangular superior Matrix

so the new equation will be (D-E-F)x=b <=> Dx =(E+F)x + b
                                       <=> x =D(-1)(E+F)x + D(-1)b
                                       <=> x =(I - D(-1)A) x + D(-1)b
                                       <=> x =B x + f

with D(-1) is the inverse of D, B = (I - D(-1)A) and f = D(-1)b

so the beautiful idea is to think that a sequence of vectors Un exist
that     Verify Un+1 = B*Un + f and  that Un converge to the x we are 
trying to find 

we have a theorem who says that under
some conditions Un converge to the x 

we chose U0 for example(1,1.(n-3)times,1) and we iterate until Un+1 -Un tends to Epsilon
close to 0 then our Un+1 is our x

#####################################################################
##3- Gauss Seidel Method

this method is nearly as the same as jacobi method, we just choose diferent
matrix to iterate the sequence.

let imagine we have a system writen Ax = b 

A : matrix belong to MnR defined positiv
X : Vector n dimension that we try to find
b : vector known

##Start solving

so let decompose A = D - E - F

D : Diagonal matrix
E : Triangular inferior Matrix
F : Triangular superior Matrix

we put P = D - E is also a triangular inferior matrix

with P(-1) is the inverse of P,  B = P(-1)F and f = P(-1)b
so the new equation will be (D-E-F)x=b <=>  (D - E)x = Fx + b
                                       <=>       Px = Fx + b
                                       <=>        x = P(-1)Fx + P(-1)b
                                       <=>        x = B x + f

we just need that A to be defined and positiv to have convergence

#####################################################################
##4- Gradient Method

Hold yourself Gradient method is comming

Gradient method is easy to implement but difficult to understand, it was
difficult from the book and wikipedia, i will try to explain the idea of 
the theory and then i will just try to explain the algorithme, i  associate
wikepdia links for more explanations https://fr.wikipedia.org/wiki/Algorithme_du_gradient

############Theorical explanations###########

if you don't hunderstand that part jump to algorithmic explanation
 
A : matrix belong to MnR defined positiv and symetric
X : Vector n dimension that we try to find
b : vector known


1-so we have a system Ax = b <=> Ax - b = 0

2- we associate to that system a function from R^n to R which represent 
the "enrergy" of the system, this function is E(x) = 1/2 x(T)Ax - x(T)b  | with x(T) means transposed of x

that E(x) has a particularity tat grad(E(x)) = Ax - b, it's our system

3-solving the problem would be equivalent to MINIMIZE energy E(X), so :

3.1-we will choose an arbitrary point int the space that we are working on
3.2-we consider that that point belong to an hyperspace
(means a space with a dimension less of space we are woring on)
that hyperspace represent a constant level of energy, so if x belong to that 
hyperspace => dE(x) = 0 /d() is diferential
3.3-this hyperspace if we would draw it, we would use the equation dE(x) = <grad(E(x))|dOM>
3.4-what grad(E(x)) gives as, is the local direction of how energy increase, so - grad(Ex)
is the local direction of how energy decrease
3.5- so we came up with the idea to jump for a level of energy, to another one, 
from an hyperspace to another one, how contain less energy, until we rich E(x) = 0



2D example

we imagine that each level of energy correspond to a curve for example an eleptycal one in 2 dimension x1, y1

each level represent an energy or a potential, and whetever we are in a finit position in space we belong to a 
level of energy, the idea is to go from the level that correspond to (x1,y1) to the level below that correspond
to the level (x2,y2) until beeing in the minimul Level where we have grad(E(xmin,ymin)) = 0
   
so we in that process we will have the equation Xn+1 - Xn = - ak grad(E(Xn)) 
we will iterate until grad(E(Xn)) --> 0                                       
        _________________
       /                 \
      /                   \
     /   _____________     \
    /   /             \     \
       /               \    \
               .           
   \   \               /   /
    \   \_____________/   /
     \                   /
      \_________________/
############Algorithmic explanations###########

as in the previous method we have sequence that converge

Un+1 - Un = - ak grad(E(Un))

we put r = grad(E(Un) / r the residu

with ak have a specefic value ak = rk(T) * rk / rk(T) A r(k)

#####################################################################
##5- conjugate_gradient Method

This method is a really beautiful evolution of the normal gradient method.
in wikipedia they give an idea of explanation and they give an algorithm
that does not follow explanation,it is an optimized one, and its explanation
is given in the link 1.

i tried to implement the algorithm explained, but i didnt
get the expected result so i gave up after several tries

so we will just reimplement the algo given in wikipedia


############Theorical explanations###########
useful links:
1-http://www.math.univ-montp2.fr/~di-pietro/ON/lecture9.pdf
2-https://en.wikipedia.org/wiki/Conjugate_gradient_method


