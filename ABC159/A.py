def main():
    N, M = map(int, input().split())
    
    ans = 0
    if N >= 2:
        ans += N*(N-1)/2
    
    if M >= 2:
        ans += M*(M-1)/2

    print(int(ans))

if __name__ == '__main__':
    main()

"""
import sys
input = sys.stdin.readline

A,B = map(int, input().split())
N = list(map(int, inputs().split()))
M = [int(input()), for _ in range(N)]
"""