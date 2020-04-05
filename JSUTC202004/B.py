def main():
    N = int(input())

    x_r = []
    x_b = []
    for _ in range(N):
        x, c = input().split()
        if c == 'B':
            x_b.append(int(x))
        if c == 'R':
            x_r.append(int(x))
    
    if len(x_r) != 0:
        x_r.sort()
        for x in x_r:
            print(x)
    
    if len(x_b) != 0:
        x_b.sort()
        for x in x_b:
            print(x)

if __name__ == '__main__':
    main()