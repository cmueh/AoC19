def never_decrease(num):
    s = str(num)
    return list(s) == sorted(s)


def two_adj(num):
    d = {}
    for i in "0123456789":
        d[i] = 0

    for i in str(num):
        d[i] += 1

    return max(d.values()) >= 2

sum = 0
for i in range(372037, 905157+1):
     if never_decrease(i) and two_adj(i):
         sum+= 1

print(sum)

