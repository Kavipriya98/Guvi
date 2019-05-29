def product(N):
  result=1
  while(N!=0):
    X=N%10
    result=result*X
    N=N//10
  print(result)
N=int(input(""))
product(N)
