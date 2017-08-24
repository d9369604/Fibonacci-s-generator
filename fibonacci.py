def fib():
    a, b = 0, 1
    while True:
        fibonacci_num = a + b
        yield fibonacci_num
        a, b = b, fibonacci_num
