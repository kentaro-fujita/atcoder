n = int(input())

lb, ub = 0, n
print(lb, flush=True)
s = str(input())
if s == 'Vacant':
    exit()
for i in range(19):
    mid = (lb + ub) // 2
    print(mid, flush=True)
    t = str(input())
    if t == 'Vacant':
        exit()
    if (mid - lb) % 2 == 0 and s == t:
        lb = mid
    elif (mid - lb) % 2 == 0 and s != t:
        ub = mid
    elif s == t:
        ub = mid
    else:
        lb, s = mid, t
