sx, sy, tx, ty = map(int, input().split())
dx = tx - sx
dy = ty - sy

res = ""
for i in range(dy): res += "U"
for i in range(dx): res += "R"
for i in range(dy): res += "D"
for i in range(dx): res += "L"

res += "L"
for i in range(dy+1): res += "U"
for i in range(dx+1): res += "R"
res += "D"
res += "R"
for i in range(dy+1): res += "D"
for i in range(dx+1): res += "L"
res += "U"

print(res)
