def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sumA = sum(A)
    
    ans = True
    for i in range(M):
        if (A[i] < sumA /(4*M)):
            ans = False

    if ans:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

"""
import sys
input = sys.stdin.readline

A,B = map(int, input().split())
N = list(map(int, inputs().split()))
M = [int(input()), for _ in range(N)]
"""