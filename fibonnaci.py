def fibonnaci(N):
  if(N<2):
    return 1
  return(fibonnaci(N-1)+fibonnaci(N-2))
N=int(input(""))
for i in range(N):
  print(fibonnaci(i))
