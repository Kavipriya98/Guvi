def mul(N):
  M=N//10
  if(N<10):
    print("10")
  else:
    M=(M+1)*10
    print(M)
N=int(input(""))
mul(N)
