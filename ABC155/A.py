def main():
    A, B, C = input().split(' ')

    if A == B and B == C:
        print('No')
    elif A == B:
        print('Yes')
    elif B == C:
        print('Yes')
    elif A == C:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
