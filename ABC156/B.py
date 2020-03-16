def main():
    N, K = map(int, input().split(' '))

    i = 0
    while True:
        if N  >= pow(K,i):
            i += 1
        else:
            break

    print(i)
 
if __name__ == '__main__':
    main()


"""
A, B = map(int, input().split(' '))
N = list(map(int, input().split(' ')))
"""