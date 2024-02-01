n,k,q = map(int, input().split())
qu = []
l = list(map(int, input().split()))
for i in range(q):
    a = int(input())
    qu.append(a)

for i in range(k):
    l.insert(0, l[-1])
    l.pop()

for i in qu:
    print(l[i])
