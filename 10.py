def c(n, m):
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0
    return c(n - m, m - 1) + c(n, m - 1)

n = int(input())
print(c(n, n - 1))
