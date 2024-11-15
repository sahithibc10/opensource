n=int(input())
i=int(input())
r=1<<(i-1)
if(n&r)!=0:
    print("true")
else:
    print("false")
