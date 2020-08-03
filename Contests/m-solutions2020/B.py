import copy

cards = list(map(int, input().split()))
k = int(input())

ans = set()
for i in range(3**k):
    n = i
    s = []
    while n:
        s.append(n % 3)
        n //= 3
    m = len(s)
    res = 0
    cards_copy = copy.deepcopy(cards)
    for j in range(m):
        cards_copy[s[j]] *= 2
    a, b, c = cards_copy
    if a < b < c:
        print("Yes")
        exit()
print("No")
