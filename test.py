def count_down(n):
    while n > 0:
        yield n
        n -= 1

for num in count_down(5):
    print(num)