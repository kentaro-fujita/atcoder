def main():
    S = input()
    Q = int(input())
    S_reverse = S[::-1]

    for i in range(Q):
        q = list(input().split(' '))
        if len(q) > 1:
            if q[1] == '1':
                S = q[2] + S
                S_reverse = S_reverse + q[2] 
            elif q[1] == '2':
                S = S + q[2]
                S_reverse = q[2] + S_reverse
        elif q[0] == '1':
            temp = S_reverse
            S_reverse = S
            S = temp

    print(S)

if __name__ == '__main__':
    main()

"""
A,B = map(int, input().split(' '))
N = list(map(int, inputs().split(' ')))
"""