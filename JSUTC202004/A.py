def main():
    S, L, R = map(int, input().split())

    if L <= S and S <= R:
        print(S)
    elif abs(S-L) <= abs(S-R):
        print(L)
    elif abs(S-L) > abs(S-R):
        print(R)

if __name__ == '__main__':
    main()