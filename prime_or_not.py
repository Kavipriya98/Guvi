N=int(input(""))
com=0
for i in range(2,N):
  if(N%i==0):
    com=1
    break
if(com==1):
  print("no")
else:
  print("yes")
