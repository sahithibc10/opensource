n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]
mirror=[r[::-1] for r in matrix]
for r in mirror:
    print(*r)
