def giaithua(n):
    giaithua=1
    if (n==1) or (n==0):
        return gt 
    else:
        for i in range(2,n+1,1):
            giaithua*=i
        return giaithua

n=int(input())
print(giaithua(n))