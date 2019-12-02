f = open('input.txt')

arr = [(int(x.strip())) // 3 - 2 for x in f.readlines()]
print(sum(arr))
