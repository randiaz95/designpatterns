memoization = {}
def fib(n):
    if n in memoization:
        return memoization[n]
    if n <= 2: return 1
    total = fib(n-1) + fib(n-2)
    memoization[n] = total
    return total


if __name__ == '__main__':
    print(fib(50))