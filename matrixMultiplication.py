def initialize_mat(dim):
  c=[]
  for i in range(dim):
    c.append([])
  for i in range(dim):
    for j in range(dim):
      c[i].append(0)
  return(c)
  
  
def dot_product(u,v):
  dim=len(u)
  sum=0
  for i in range(dim):
    sum=sum+(u[i]*v[i])
  return(sum)


def row(M,i):
  l=[]
  dim=len(M)
  for k in range(dim):
    l.append(M[i][k])
  return l


def column(M,j):
  l=[]
  dim=len(M)
  for k in range(dim):
    l.append(M[k][j])
  return l
M=[[1,2,3],[4,5,6],[7,8,9]]



def mat_mul(A,B):
  dim=len(A)
  C=initialize_mat(dim)
  for i in range(dim):
    for j in range(dim):
      C[i][j]=dot_product(row(A,i),column(B,j))
  return(C)



#using numpy
import numpy
a=[[0,1,2],[3,4,5],[6,7,8]]
b=[[9,10,11],[12,13,14],[15,16,17]]
print(a)
a=numpy.mat(a)
b=numpy.mat(b)
c=a*b
print(c)
for i in c:
  print(i)
