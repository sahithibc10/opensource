x=int(input())
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")
