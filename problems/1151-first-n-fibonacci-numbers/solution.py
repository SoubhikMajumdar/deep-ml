def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    i = 0
    fib = []
    while i < n:
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[-2] + fib[-1])
        
        i+=1

    return fib

