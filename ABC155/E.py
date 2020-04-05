def main():
    N = input()

    a = 0
    b = 0

    t = int(N[-1])
    a, b = a + t, a + (10 - t)

    for i in range(len(N) - 2, -1, -1):
        t = int(N[i])
        a, b = min(a + t, b + (t + 1)), min(a + (10 - t), b + (10 - (t +1)))

    print(min(a, b + 1))

if __name__ == '__main__':
    main()