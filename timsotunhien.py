def f(x):
    return x**2- 100*x +1
a=list(map(int,input().split()))
dem=0
mang=[]
for i in range(a[0],a[1]+1,1):
    b=f(i)
    if b>a[1]:
        break
    else:
      if b<=a[1] and b>=a[0]:
        dem+=1
        mang.append(i)
if dem>0:
    print(dem)
    for i in mang:
      print(i,end=' ')
else:
    print('vn')





