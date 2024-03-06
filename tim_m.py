#tìm số m lớn nhất sao cho 1+2+..+m<x, nếu x<=1 thì trả về -1
def f(x):
    
    if x<=1:
        return -1
    else:
        s=0
        i=1
        while True:
            s+=i
            if s>=x:
                break
            else:
                i+=1
        return (i-1)
        
x=int(input())
print(f(x))