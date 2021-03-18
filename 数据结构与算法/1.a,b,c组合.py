#如果 a+b+c=100，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
import time
start_time=time.time()
for a in range(0,101):
    for b in range(0,101):
        for c in range(0,101):
            if a+b+c==100 and a**2+b**2==c**2:
                print('a:',a,'b:',b,'c:',c)
#f(n)=n*n*n*2
#获取时间
end_time=time.time()
print('所花费时间：',(end_time-start_time))