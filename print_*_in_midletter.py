def fnc(S):
  x=len(S)
  y=x//2
  if (x%2)!=0:
    print(S[0:y],end=""),print('*',end=""),print(S[y+1:x+1],end="")
  else:
    print(S[0:y-1],end=""),print('**',end=""),print(S[y+1:x+1],end="")
S=input("")
fnc(S)
