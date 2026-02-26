def squares(n):
    for i in range(n):
        yield i*i

for s in squares(5):
    print(s)