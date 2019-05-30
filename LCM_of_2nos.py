N,M=map(int,input().split())
if(N>M):
  min=N
else:
  min=M
while(1):
  if(min%N==0 and min%M==0):
    print(min)
    break
  min=min+1
