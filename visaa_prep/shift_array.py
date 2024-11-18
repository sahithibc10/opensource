n=int(input())
arr=list(map(int,input().split()))
shift=arr[1:]+arr[:1]
print(*shift)
