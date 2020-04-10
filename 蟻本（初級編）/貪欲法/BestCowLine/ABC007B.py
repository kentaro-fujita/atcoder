a = input()

if len(a) > 1:
    print(a[:-1])
elif a == 'a':
    print(-1)
else:
    print(chr(ord(a)-1))