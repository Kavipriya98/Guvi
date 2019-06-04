def fnc(N,K,n):
  if K in n:
    print("yes")
  else:
    print("no")
N,K=input().split()
n=list(map(str,input().split()))
fnc(N,K,n)
