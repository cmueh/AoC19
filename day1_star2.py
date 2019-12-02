f = open('input.txt')


def calc(n):
    s = 0

    while True:
        v = n // 3 - 2
        if v <= 0:
            break
        s += v
        n = v

    return s

arr = [calc(int(x.strip())) for x in f.readlines()]
print(sum(arr))
