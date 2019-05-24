ch=input("")
if(ch>='A' and ch<='Z' or ch>='a' and ch<='z'):
  if(ch=='A' or ch=='E' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Invalid")
