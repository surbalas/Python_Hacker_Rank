# Import Collections Module
from collections import Counter
# Input Number of Shoes
X = int(input())
# Sizes of Shoes in the shop
sz = list(map(int,input().split()))
# Number of Customers
N = int(input())
# Customer shoe size and prize
css = []
spr = []
for i in range(N):
    cs, pr = map(int,input().split())
    css.append(cs)
    spr.append(pr)
ssdict = Counter(sz)
print(ssdict)
total_earned = 0
for ix,elem in enumerate(css):
    if(elem in ssdict.keys()):
        if(ssdict[elem] > 0):
            total_earned += spr[ix]
            ssdict[elem] -= 1
        else:
            print("Size",elem,"no longer available, so no purchase")
    else:
        print("Size",elem,"not available, so no purchase")
print(total_earned)
