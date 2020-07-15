import math


def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]

    max_distance = 0
    for i in range(N):
        for j in range(N):
            x1, y1 = xy[i]
            x2, y2 = xy[j]

            distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            if max_distance < distance:
                max_distance = distance

    print(max_distance)


if __name__ == '__main__':
    main()
