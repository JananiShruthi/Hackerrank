def diff(ele, s):
    for i in s:
        if abs(ele - i) > 1:
            return False
    return True

n = int(input())
l1 = list(map(int, input().split()))
l1.sort()
subsets = [] #This is a list for having all the subarrays with abs diff <= 1 
s = []
for i in range(n):
    if len(s) == 0:
        s.append(l1[0])
    else:
        if diff(l1[i], s):
            s.append(l1[i])
            #print(f"APPENDING:{l1[i]}")
            #print("S after appending: ", s)
        else:
            subsets.append(s)
            #print("Now subsets are: ", subsets)
            s = [l1[i]]
            #print("S: ", s)

if s:
    subsets.append(s)

#print(subsets)

m = max(len(i) for i in subsets)
print(m)