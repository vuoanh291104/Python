
n=int(input())
a=list(map(int,input().split()))
b=[]
sl=0
for i in a:
    if i>0:
        b.append(i)
        sl+=1
if sl>0:
    print(sl)
    for i in b:
        print(i,end=' ')
else:
    print('khong co phan tu duong')





        

