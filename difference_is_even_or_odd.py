def diff(N,M):
  Z=N-M
  if(Z%2==0):
    print("even")
  else:
    print("odd")
N,M=map(int,input().split())
diff(N,M)
