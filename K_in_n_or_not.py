def fnc(N,K,n):
  if K in n:
    print("Yes")
  else:
    print("No")
N,K=input().split()
n=list(map(str,input().split()))
fnc(N,K,n)
