def fnc(N):
  sum=0
  while(N>0):
    x=N%10
    sum=sum+x
    N=N//10
  print(sum)
N=int(input(""))
fnc(N)
