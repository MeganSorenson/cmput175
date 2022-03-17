def foo(n, m):
    if (n - m) < 0:
        answer = 0
    else:
        answer = 1 + foo(n - m, m)
    return answer


print(8 - 4)
print(foo(8, 4))
print(9 // 2)
print(foo(9, 2))
