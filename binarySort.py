def binarysort(l,k):
  begin=0
  end=len(l)-1
  
  while ((end-begin)>1):
    mid=(end+begin)//2
    if l[mid]==k:
      return 1
    if l[mid]>k:
      end=mid-1
    if l[mid]<k:
      begin=mid+1
  if (l[begin]==k) or (l[end]==k):
    return 1
  else:
    return 0
