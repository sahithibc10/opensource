n=int(input())
stick=list(map(int,input().split()))
stick.sort(reverse=True)
for i in range(n-2):
    if stick[i]<stick[i+1]+stick[i+2]:
        print(stick[i]+stick[i+1]+stick[i+2])
        break
else:
    print(-1)
