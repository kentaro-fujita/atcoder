def main():
    S = input()
    
    if S[2] == S[3] and S[4] == S[5]:
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