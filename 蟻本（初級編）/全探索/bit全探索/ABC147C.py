def judge(isHonest, judge_list):
    for j in judge_list:
        x, y = j 
        if isHonest[x-1] != y:
            return False
    return True  

def main():
    N = int(input())

    testimony = []
    for _ in range(N):
        A = int(input())
        testimony.append([list(map(int, input().split())) for _ in range(A)])
    
    ans = 0
    for i in range(2**N):
        judge_list = []
        isHonest = []
        for j in range(N):
            if i & (1 << j):
                judge_list += testimony[j]
                isHonest.append(1)
            else:
                isHonest.append(0)
        if judge(isHonest, judge_list):
            ans = max(ans, sum(isHonest))
    
    print(ans)

if __name__ == '__main__':
    main()