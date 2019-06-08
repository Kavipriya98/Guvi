import math
N,M=map(int,input().split())
Z=N*M
X=math.sqrt(Z)
if (int(X+0.5)**2==Z):
  print("yes")
else:
  print("no")
