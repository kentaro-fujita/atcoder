import math

def main():
    D, G = map(int, input().split())

    pc = [list(map(int, input().split())) for _ in range(D)]

    ans = 100**10
    for i in range(1<<D):
        score = 0
        prob = 0
        last = -1
        for j in range(D):
            p, c = pc[j]
            if i & (1<<j):
                score += (j+1)*100*p + c
                prob += p
            else:
                last = j
        if score >= G:
            ans = min(ans, prob)
            continue
        elif last == -1:
            continue
        else:
            need = math.ceil((G-score)/((last+1)*100))
            if need > pc[last][0]-1:
                continue
            else:
                ans = min(ans, prob+need)
    print(ans)


if __name__ == '__main__':
    main()