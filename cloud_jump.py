def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0
    while (i+k)%n != 0:
        if c[(i+k)%n] == 1:
            e -= 3
            print(f"e thunder : {e} at {(i+k)%n} ")
        else:
            e -= 1
            print(f"e normal : {e} at {(i+k)%n} ")
        i += k
        
    if c[0] == 1:
        return e-3
    else:
        return e-1

n = int(input())
c = list(map(int, input().split()))
k = int(input())
res = jumpingOnClouds(c, k)

print(res)