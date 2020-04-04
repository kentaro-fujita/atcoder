def main():
    X = int(input())
    
    ans = 0
    ans += (X // 500) * 1000
    X -= (X//500)*500
    ans += (X//5) * 5

    print(ans)
    

if __name__ == '__main__':
    main()

"""
import sys
input = sys.stdin.readline

A,B = map(int, input().split())
N = list(map(int, inputs().split()))
M = [int(input()), for _ in range(N)]
"""