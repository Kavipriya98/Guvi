def fnc(N,M):
  N=N^M;
  M=M^N;
  N=N^M;
  print(N,M)
N,M=map(int,input().split())
fnc(N,M)
