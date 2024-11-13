x,y,z=map(int,input().split())
a=x+y
if z>=a:
    print("2")
elif z>=x:
    print("1")
else:
    print("0")
