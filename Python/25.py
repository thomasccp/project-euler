#fib =  lambda n: n if n<2 else fib(n-1)+fib(n-2)

#i = 1
#while len(str(fib(i))) <1000:
#    i = i+1

#print fib(i-1)

a,b,cnt = 1,1,1
while True:
    a,b,cnt = b,a+b,cnt+1
    if len(str(b))>=1000:
        break

print cnt+1
