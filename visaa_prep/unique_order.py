n=int(input())
arr=list(map(int,input().split()))
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(*unique)
