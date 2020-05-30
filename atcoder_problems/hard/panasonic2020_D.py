n = int(input())

def dfs(s, mx):
    if len(s) == n:
        print(s)
    else:
        for i in range(mx + 1):
            c = chr(ord('a') + i)
            if i == mx:
                dfs(s+c, mx+1)
            else:
                dfs(s+c, mx)
dfs('', 0)
