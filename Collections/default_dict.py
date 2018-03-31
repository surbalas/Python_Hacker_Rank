from collections import defaultdict
# DefaultDict Tutorial
n, m = map(int,input().split())
# Create a Default dictionary of Lists
d = defaultdict(list)
# Appending A list to Defualt Dictionary
for i in range(n):
    d[input()].append(i + 1)

# For each word in B, find the index and
# occurence of word in A
for j in range(m):
    Bword = input()
    print(" ".join(map(str, d[Bword])) or -1)
