n=int(input())
L=[" "*(n-i)+"*"*(i)for i in range(1,n)]
for i in L:
  print(i+i[-1::-1])
L.reverse()
for i in L:
  print(i+i[-1::-1])
