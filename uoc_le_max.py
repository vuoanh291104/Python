def f(x):
    import numpy as np
    a=[]
    for i in range(1,x):
        if ((x%i==0) and (i%2!=0)):
            a.append(i)
            b=np.max(a)
    return b
x=int(input())
print(f(x))
