def fnc(S):
  s=0
  for i in S:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='o' or i=='O' or i=='u' or i=='U'):
      s=s+1
  if(s==0):
    print("no")
  else:
    print("yes")
S=input("")
fnc(S)
