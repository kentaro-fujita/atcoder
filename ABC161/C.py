def main():
    N, K = map(int, input().split())
    
    div = N // K
    min1 = abs(N - div*K)
    min2 = abs(N - (div+1)*K)

    print(min(min1,min2))

if __name__ == '__main__':
    main()

"""
import sys
input = sys.stdin.readline

A,B = map(int, input().split())
N = list(map(int, inputs().split()))
M = [int(input()), for _ in range(N)]
"""