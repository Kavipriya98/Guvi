def fnc(N):
  X=[int(i) for i in input().split()]
  X.sort()
  for i in range(N):
    print(X[i])
N=int(input(""))
fnc(N)
