n=int(input())
r=n<0
n=abs(n)
rev=int(str(n)[::-1])
if r:
    rev=-rev
if rev<-2**31 or rev>2**31-1:
    print(0)
else:
    print(rev)
