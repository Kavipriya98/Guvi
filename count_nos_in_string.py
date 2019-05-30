def fnc(N):
  X=0
  for i in N:
    if i.isnumeric():
      X=X+1
  print(X)
N=input("")
fnc(N)
