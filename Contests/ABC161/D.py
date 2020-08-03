from collections import deque


def main():
    K = int(input())

    q = deque()
    for i in range(1, 10):
        q.append(i)

    count = 0
    while (True):
        x = q.popleft()
        if x % 10 != 0:
            q.append(10*x+(x % 10)-1)
        q.append(10*x+(x % 10))
        if x % 10 != 9:
            q.append(10*x+(x % 10)+1)
        if count == K-1:
            print(x)
            break
        count += 1


if __name__ == '__main__':
    main()
