def palindrome(N):
  M=N[::-1]
  if(M==N):
    print("yes")
  else:
    print("no")
N=input("")
palindrome(N)
