def fnc(N,A,D):
  sum=0
  for i in range(0,int(N)):
    sum=sum+int(A)
    A=int(A)+int(D)
  print(sum)
N,A,D=input().split()
fnc(N,A,D)
