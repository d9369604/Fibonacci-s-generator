def fib():
    res = [0, 1]
    for i in range(2, 1000):
        res.append(res[i-2] + res[i-1])
        yield res[i]
