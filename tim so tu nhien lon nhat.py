m=float(input())
i=1
s=0
while True:
    s+=1/i
    if m<s:
        break
    else:
        i+=1
if i>1:
    print(i-1)
else:
    print('NULL')
