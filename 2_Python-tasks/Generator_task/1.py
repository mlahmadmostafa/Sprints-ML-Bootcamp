def fib_for(n):
    series = [0,1]
    for i in range(2,n):
        series.append(series[i-1]+series[i-2])
    return series
x = fib_for(10) 
print(x)


def fib(n,a=0,b=1):
    if n == 0:
        return 0
    yield a
    yield from fib(n - 1, b, a+b)

fun = fib(10)
for i in fun:
    print(i,end = ' ')
print()
print("Fibonacci with loop used", i*len(x))
print("Fibonacci with generator used", i.bit_length())
