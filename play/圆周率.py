#!/usr/bin/env python3

a = 10000
c = 2800
e = 0
f = [a // 5 for i in range(c + 1)]

while c != 0:
    d = 0
    g = c * 2
    b = c
    while True:
        d += f[b] * a
        g -= 1
        f[b] = d % g
        d //= g
        g -= 1
        b -= 1
        if b == 0:
            break
        d *= b

    c -= 14
    print("%.4d" % (e + d // a), end="")
    e = d % a
