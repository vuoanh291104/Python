a=list(map(int,input().split()))
if a[0]**2+a[1]**2==a[2]**2 or a[0]**2+a[2]**2==a[1]**2 or a[1]**2+a[2]**2==a[0]**2:
    print('YES')
else:
    print('NO')
        