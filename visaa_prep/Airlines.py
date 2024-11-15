x,n=map(int,input().split())
e=x*100
if e>=n:
    print("0")
else:
    r=n-e
    p=(r+99)//100
    print(p)
