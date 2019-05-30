def fnc(hr1,min1,hr2,min2):
  i=int(hr1)
  j=int(min1)
  k=int(hr2)
  l=int(min2)
  sub1=i-k
  sub2=j-l
  print(sub1,sub2)
hr1,min1=map(int,input().split())
hr2,min2=map(int,input().split())
fnc(hr1,min1,hr2,min2)
