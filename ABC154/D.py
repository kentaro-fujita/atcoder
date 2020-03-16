def sigma(n):
    return sum([i for i in range(n+1)])

def main():
    N, K = map(int, input().split(' '))
    p = list(map(int, input().split(' ')))

    max_value = 0
    for i in range(N-K+1):
        sum_ = sum(p[i:i+K])
        if sum_ > max_value:
            max_value = sum_
            max_list = p[i:i+K]

    expected = 0
    for v in max_list:
        expected += sigma(v) / v

    print(expected)

if __name__ == '__main__':
    main()