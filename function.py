def pyramid(n):
    for i in range(1, n+1):
        print("  " * (n-i) + " * " * (2 * i - 1))


n = 3
pyramid(n)