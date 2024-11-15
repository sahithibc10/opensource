n,x,y=map(int,input().split())
max_marks=n*x
min_marks=0
if y>max_marks or y<min_marks:
    print("NO")
else:
    if(y-min_marks)%x==0:
        print("YES")
    else:
        print("NO")
