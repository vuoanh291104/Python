n,x=map(int,(input().split()))
msv=[]
diem=[]
f=False
for i in range(0,n):
    tmsv,tdiem=map(int,input().split())
    if (tmsv==x):
        print(tdiem)
        f=True
if (f==False):
    print('no data')