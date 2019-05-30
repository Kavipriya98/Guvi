def fnc(N):
  X=0
  for i in N:
    if(not i.isalnum()):
      X=X+1
  print(X)
N=input("")
fnc(N)
