n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range (0,n):
    sum+=a[i]
av=sum/(len(a))
print('%.3f'%av)