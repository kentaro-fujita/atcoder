H, W = map(int, input().split())

ans = float("inf")
for i in range(1, H):
    h = H - i
    s1 = [i * W, h // 2 * W, (h - h // 2) * W]
    if 0 not in s1: ans = min(ans, max(s1)-min(s1))
    s2 = [i * W, W // 2 * h, (W - W // 2) * h]
    if 0 not in s2: ans = min(ans, max(s2) - min(s2))

for i in range(1, W):
    w = W - i
    s1 = [i * H, w // 2 * H, (w - w // 2) * H]
    if 0 not in s1: ans = min(ans, max(s1)-min(s1))
    s2 = [i * H, H // 2 * w, (H - H // 2) * w]
    if 0 not in s2: ans = min(ans, max(s2) - min(s2))

print(ans)
