n = int(input())
l = list(map(int, input().split()))
x = 1
for i in range(n):
    index = l.index(x)
    val = l.index(index + 1)
    print(val + 1)
    x += 1