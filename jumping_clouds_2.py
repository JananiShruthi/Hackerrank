n = int(input())
l = list(map(int, input().split()))

pos = 0
jumps = 0

while pos != (n-1):
    if l[pos + 1] == 1 and pos != n-2:
        pos = pos + 2
        jumps += 1
    elif pos == (n-2):
        pos += 1
        jumps += 1
    elif l[pos + 1] == 0 and l[pos + 2] == 0:
        pos = pos + 2
        jumps += 1
    elif l[pos + 1] == 0 and l[pos + 2] == 1:
        pos = pos + 1
        jumps += 1


print(jumps)



