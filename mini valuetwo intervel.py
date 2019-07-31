v,k=map(int,input().split())
h=(input().split())[0:v]
i=0
while i<k:
  v,n=map(int,input().split())
  i+=1
  print(min(h[v-1:n]))
