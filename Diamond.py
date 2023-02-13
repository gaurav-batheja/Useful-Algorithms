n=int(input())#min 3
L=[" "*(n-i)+"* "*(i)for i in range(1,n)]
print()
for i in L:
  print(i)
L.remove(L[-1])
L.reverse()
for i in L:
  print(i)
