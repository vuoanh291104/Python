
n=int(input())
if n==0:
    print('vui long nhap so nguyen duong')
elif n<2:
    print('khong')
elif n==2:
    print('co')
else:
    for i in range(2,n//2 +1):
        if n % i ==0:
            print('khong')
            break
    else:
            print('co')