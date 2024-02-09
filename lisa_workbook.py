n = int(input("Enter the no. of chapters: "))
k = int(input("Enter the no. of problems that a page can hold: "))

l = list(map(int, input("Enter the no of probs for each chapters").split()))

ch = 0
pg = 1
d = {}
special_prob = 0
temp = 0
while l:
    if l[ch] <= k:
        d[pg] = [i for i in range(temp+1, l[ch] + temp + 1)]
        l.pop(0)
        temp = 0
    else:
        l[ch] -= k
        d[pg] = [i for i in range(temp + 1, temp+k+1)]
        temp = d[pg][-1]
    
    if pg in d[pg]:
        special_prob += 1
    pg += 1


print("Allocated problems: ", d)
print("No. of special problems: ", special_prob)

