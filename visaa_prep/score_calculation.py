T=int(input())
for i in range(T):
    x,n=map(int,input().split())
    point=x//10
    score=n*point
    print(score)
