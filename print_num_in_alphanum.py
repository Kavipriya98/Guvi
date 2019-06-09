def fnc(S):
  Z=""
  for i in S:
    if i.isnumeric():
      Z=Z+i
  print(Z)
S=input("")
fnc(S)
