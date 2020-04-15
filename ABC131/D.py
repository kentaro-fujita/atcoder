N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB = sorted(AB, key=lambda x : x[1])

current_time = 0
for A, B in AB:
    current_time += A
    if current_time > B:
        print("No")
        exit()

print("Yes")