#Viết đường thẳng và tính y^
import math
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))
ymu=[]
SSxy=0
SSx=0
tamx=0
tamy=0
for i in range (0,n,1):
    tamx+= x[i]
    tamy+= y[i]

xtb=tamx/len(x)
ytb=tamy/len(y)

    
for i in range (0,n,1):
    SSxy+= (x[i]-xtb)*(y[i]-ytb)
    SSx+= pow((x[i]-xtb),2)
B1= SSxy/SSx
B0= ytb-B1*xtb
for i in range(0,n,1):
    ym=B0 + B1*x[i]
    ymu.append(ym)
print("Y MU: ",ymu)

print("B1: ",B1)
print("B0: ",B0)
#tính sai số
yy=0
yyy=0
for i in range(0,n,1):
    yy+=abs(y[i]-ymu[i])
    yyy+=pow((y[i]-ymu[i]),2)
MAE=(1/n)*yy
MSE=(1/n)*yyy
RMSE=pow(MSE,0.5)
print("MAE: ",MAE)
print("MSE: ",MSE)
print("RMSE: ",RMSE)
#tính R-quared( R^2)
SSR=0
SST=0
for i in range(0,n,1):
    SSR+=pow((ymu[i]-ytb),2)
    SST+=pow((y[i]-ytb),2)
R_binh= SSR/SST
print("SSR: ", SSR)
print("SST: ",SST)
print("R^2: ",R_binh)


