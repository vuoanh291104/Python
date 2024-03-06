a=list(map(float,input().split()))
delta=pow(a[1],2)-4*a[0]*a[2]
if a[0]==0:
  if a[1]==0:
    if a[2]==0:
      print('vo so nghiem')
    else:
      print('vo nghiem')
  else:
    print('%.3f'%(-a[2]/a[1]))
else:
  if delta<0:
    print('vo nghiem')
  elif delta==0:
    print('%.3f'%(-a[1]/(2*a[0])))
  else:
    b=[]
    b.append((-a[1]-pow(delta,0.5))/(2*a[0]))
    b.append((-a[1]+pow(delta,0.5))/(2*a[0]))
    b.sort()
    print('%.3f'%b[0],end=' ')
    print('%.3f'%b[1])
    