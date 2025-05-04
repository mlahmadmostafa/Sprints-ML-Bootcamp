def factorial(n):
    if n < 0:
        return 0
    if n <= 1: 
        return 1
    return n * factorial(n - 1) # n! = n * (n-1)!

while True:
    try:
        fib = factorial(int(input())) # calculating fibonacci
    except ValueError: # Handling non int inputs
        print("Invalid input")
        continue
    if fib==0: # Handling negative inputs
        print("Invalid input")
        continue
    print(fib)

