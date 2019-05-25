N,Q=map(int,input().split())
for i in range(N+1,Q):
  s=0
  temp=i
  while(temp>0):
    r=temp%10
    s=s+(r**3)
    temp=temp//10
  if(i==s):
    print(i)
