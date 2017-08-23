def fib():
    base_num = [0, 1]
    while True:
        fibonacci_num = sum(base_num)
        yield fibonacci_num
        base_num.pop(0)
        base_num.append(fibonacci_num)
