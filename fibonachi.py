def loop():
    x = int(input("enter:"))
    before_1 = 0
    before_2= 1
    next_num = 1
    count  = 1
    while count <= x :
        print(next_num)
        next_num = before_1 + before_2
        count += 1
        before_1 = before_2
        before_2= next_num
loop()
#######################################
def fibo(x,a=0,b=1,count=1):
    if count<=x:
        print("-------------------------")
        print(b)
        c=a+b
        count+=1
        return fibo(x,b,c,count)
fibo(5)

