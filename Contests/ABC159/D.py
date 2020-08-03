from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    count = Counter(A)
    sum_ = sum([v*(v-1)/2 for v in count.values()])

    for i in range(len(A)):
        took_count = count[A[i]]
        sub = took_count - 1
        print(int(sum_ - sub))


if __name__ == '__main__':
    main()
