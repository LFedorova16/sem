import itertools
alf = input().split()
n = int(input())
for combo in itertools.product(alf, repeat=n):
    print("".join(combo))
