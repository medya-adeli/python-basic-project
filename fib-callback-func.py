def fibo(x,a=0,b=1,count=1):
    if count<=x:
        print(b)
        c=a+b
        count+=1
        return fibo(x,b,c,count)
fibo(5)