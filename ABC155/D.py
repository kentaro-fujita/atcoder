import numpy as np

def main():
    N, K = map(int, input().split())
    A = np.array(input().split(), np.int64)
    A.sort()

    zero = A[A == 0]
    neg = A[A < 0]
    pos = A[A > 0]

    print(neg)

if __name__ == '__main__':
    main()

"""
A, B = input().split(' ')
A, B = map(int, input().split(' '))
N = list(map(int, input().split(' ')))
"""