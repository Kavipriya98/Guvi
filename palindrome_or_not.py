N=int(input(""))
temp=N
rev=0
while(N!=0):
  x=N%10
  rev=(rev*10)+x
  N=N//10
if(temp==rev):
  print("yes")
else:
  print("no")
