a, b, c = map(int, input().split())

if 4 * a * b < (c-a-b)**2 and a+b < c:
    print("Yes")
else:
    print("No")
