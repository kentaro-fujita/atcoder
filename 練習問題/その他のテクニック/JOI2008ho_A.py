n = int(input())

stack = []
old = None
for i in range(n):
    s = int(input())
    if i % 2 == 1:
        if old != s:
            stack.pop()
            if len(stack) == 0:
                stack.append(0)
    else:
        if old != s:
            stack.append(i)
    old = s

if old == 0:
    stack.append(i+1)

if len(stack) % 2 == 1:
    stack.insert(0, 0)

print(sum(stack[1::2]) - sum(stack[::2]))
