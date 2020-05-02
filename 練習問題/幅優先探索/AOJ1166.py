from collections import deque

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    
    col = []
    row = []
    for i in range(h-1):
        col.append(list(map(int, input().split())))
        row.append(list(map(int, input().split())))
    
    s = [[0] * w for _ in range(h)]
    que = deque([(0, 0)])
    