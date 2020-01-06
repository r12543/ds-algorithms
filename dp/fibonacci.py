series = [0, 1]


def update_fibo(start, end):
    for i in range(start, end + 1):
        series.append(series[i-1] + series[i-2])


def fibonacci(n):
    if n >= len(series):
        update_fibo(len(series), n)
    return series[n]


N = 15
for i in range(N+1):
    print(fibonacci(i))
