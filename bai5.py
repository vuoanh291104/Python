#kiem tra xem co phai nam nhuan khong
nam=int(input('nhao vao nam:'))
if (nam % 400==0) or (nam % 4==0 and nam %100!=0):
    print(nam,'la nam nhuan')
else:
    print(nam,'khong la nam nhuan')
