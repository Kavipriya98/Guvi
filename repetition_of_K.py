def fnc(N,K,x):
  count=0
  for i in range(0,len(x)):
    if(x[i]==K):
      count=count+1
  print(count)
N,K=input().split()
x=list(map(str,input().split()))
fnc(N,K,x)
