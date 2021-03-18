def fac(n):
    if n == 1:
        return 1
    else:
        res = n * fac(n - 1)
        return res


# print(fac(6))


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(50))
