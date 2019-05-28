def fnc(N):
  if(N>1):
    for i in range(2,N):
      if(N%i==0):
        print("no")
      else:
        print("yes")
N=int(input(""))
fnc(N)
