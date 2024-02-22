import math

n = int(input())
shared = 5
cumulative = 0
for i in range(n):
    #print("Day: ", i+1)
    liked = math.floor(shared/2)
    cumulative += liked
    #print("Shared: ", shared, " Liked: ", liked, " cumulative: ", cumulative)
    shared = liked * 3

print(cumulative)