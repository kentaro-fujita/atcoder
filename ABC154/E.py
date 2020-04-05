def main():
    N = int(input())
    K = int(input())

    b = []
    for i in range(10**(K-1), 10**K):
        if '0' not in str(i):
            b.append(i)

    print(len(b))

if __name__ == '__main__':
    main()