def check(string):
    reversed_string = list(reversed(string))
    if list(string) == reversed_string:
        return True
    else:
        return False

def main():
    S = input()
    N = len(S)

    part1 = S[:int((N-1)/2)]
    part2 = S[int((N+3)/2)-1:]

    if check(S) and check(part1) and check(part2):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

"""
import sys
input = sys.stdin.readline

A,B = map(int, input().split(' '))
N = list(map(int, inputs().split(' ')))
M = [int(input()), for _ in range(N)]
"""