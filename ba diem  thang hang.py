from math import sqrt
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ab=sqrt(pow((b[0]-a[0]),2) + pow((b[1]-a[1]),2))
bc=sqrt(pow((c[0]-b[0]),2) + pow((c[1]-b[1]),2))
ac=sqrt(pow((c[0]-a[0]),2) + pow((c[1]-a[1]),2))
if ab + bc==ac or bc + ac==ab or ab  +ac==bc:
  print('YES')
else:
  print('NO')