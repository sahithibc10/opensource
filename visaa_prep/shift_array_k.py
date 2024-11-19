n=int(input())
arr=list(map(int,input().split()))
k=int(input())
k=k%n
r=arr[-k:]+arr[:-k]
print(*r)
