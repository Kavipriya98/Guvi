def fnc(N):
  X=[int(i) for i in input().split()]
  X.sort()
  Z=len(X)//2
  print(X[Z])
N=int(input(""))
fnc(N)
