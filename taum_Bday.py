t = int(input())
for i in range(t):
    b,w = map(int, input().split())
    bc, wc, z = map(int, input().split())
    
    tot_amt = 0

    if bc > wc + z:
        tot_amt = (b+w)*wc + b*z
    elif bc + z < wc:
        tot_amt = (b+w)*bc + w*z
    else:
        tot_amt = b*bc + w*wc

    print(tot_amt)