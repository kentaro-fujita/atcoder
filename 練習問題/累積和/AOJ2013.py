MAX = 24*60**2 + 60*60 + 60

def datetime2second(datetime):
    hours, minutes, seconds = map(int, datetime.split(':'))

    return hours * 60**2 + minutes * 60 + seconds

while True:
    n = int(input())
    if n == 0: break

    s = [0] * (MAX + 1)
    for i in range(n):
        d, a = map(datetime2second, input().split())

        s[d] += 1
        s[a] -= 1
    
    ans = s[0]
    for i in range(MAX):
        s[i+1] += s[i]
        ans = max(ans, s[i+1])

    print(ans)
