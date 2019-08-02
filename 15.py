n=int(input())
o=list(map(int,input().split()))[0:n]
o.sort(reverse=True)
i=0
while i<n:
    print(o[i],"",end="\n")
    i+=1
