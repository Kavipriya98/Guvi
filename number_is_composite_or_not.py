def composite(N):
  x=0
  for i in range(2,N):
    if(N%i==0):
      x=1
  if(x==0):
    print("no")
  else:
    print("yes")
N=int(input(""))
composite(N)
