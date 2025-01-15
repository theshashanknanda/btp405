def fib(n):
    if(n < 0):
        return []
    n1 = 0
    n2 = 1
    arr = [0, 1]

    for i in range(n):
        n1, n2 = n2, n1 + n2

        if(n2 < 10):
            arr.append(n2)
        else:
            break

    return arr

print(fib(10))
