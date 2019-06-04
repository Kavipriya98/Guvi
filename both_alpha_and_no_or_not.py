def fnc(S):
  x=0
  y=0
  for i in S:
    if i.isnumeric():
      x=1
    if i.isalpha():
      y=1
  if(x==1 and y==1):
    print("Yes")
  else:
    print("No")
S=input("")
fnc(S)
