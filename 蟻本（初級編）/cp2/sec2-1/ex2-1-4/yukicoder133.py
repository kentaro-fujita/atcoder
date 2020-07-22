from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
win = 0
for hands_a in permutations(a, n):
    for hands_b in permutations(b, n):
        cnt += 1
        cnt_a = 0
        cnt_b = 0
        for i in range(n):
            if hands_a[i] > hands_b[i]:
                cnt_a += 1
            if hands_a[i] < hands_b[i]:
                cnt_b += 1
        if cnt_a > cnt_b:
            win += 1

print(win/cnt)
