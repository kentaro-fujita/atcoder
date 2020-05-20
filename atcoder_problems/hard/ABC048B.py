a, b, x = map(int, input().split())

low = (a-1) // x
up = b // x

print(up-low)
